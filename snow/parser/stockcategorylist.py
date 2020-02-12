# 香港 每日持股
# 上海，深圳

import sys
import os
sys.path.append(os.getcwd())
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb() 
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog
from threading import Thread

no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['symbol']  

logger = getLog('parser', 'stockcategorylist');


def getAll(categorycode,source): 
    path = fs_config['root'] + "/stockcategorylist"+source+"/" + categorycode
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            getHtml(categorycode, fullpath)
             

                
def getHtml(categorycode, fullpath): 
    global no_record
    global not_updated
    global not_change
    global added
    
    logger.info('load file:' + fullpath)
    fd = open(fullpath, 'r') 
    txt = fd.read() 
     
    html = BeautifulSoup(txt, 'html.parser')
    
   
    trs = html.find_all('tr')
    if trs != None :
        if len(trs)<=1:
            no_record = no_record + 1
            return
        for i in range(1, len(trs)):  
            tds = trs[i].findAll('td')
            if len(tds)<=2:
                continue
            
            code = str.strip(tds[1].text)
            coders = query_symbol(code)
            
            
            if coders != None and len(coders)>0: 
                symbol = coders[0]['symbol'];
                stock = {'symbol':symbol}
               
                dbrs = query_npool(symbol,categorycode)     
                if len(dbrs) == 0:
                        insert(stock, categorycode)
                        added = added + 1  
                else:
                    if isSame(dbrs[0], stock) == False:
                        logger.info ("<!------------------------ant from: " + fullpath)
                        logger.info (stock)                  
                        logger.info (dbrs[0])
                        logger.info ("database record end ------------need check----------------> ")
                        not_change = not_change + 1
                    else:
                        not_updated = not_updated + 1 
            else:
                no_record = no_record + 1   
                logger.error ("code not found symbol:"+code)  
                
    else:
        no_record = no_record + 1
    return  


def parseNumberstr(ss):
    sx = str.strip(ss).replace(',', '').replace('%', '')
    if sx == '':
        return 0
    return float(sx)
    
 
def isSame(dbrs, record):
    global fields 
    for f in fields:
        if type(record[f]) == float:
            if  record[f] != dbrs[f] :
                return False;
        if type(record[f]) == int:
            if  record[f] != dbrs[f] :
                return False;    
        else:    
            if  str(record[f]) != str(dbrs[f]) :
                return False;
 
    return True;


def insert(record, categorycode):
    # add more args 
    _args = [categorycode]
    global fields
    for f in fields:
        _args.append(record[f])
    _sql = "INSERT INTO `snow`.`shares_category_mapping` (`categorycode`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(symbol, categorycode): 
    _sql = "select * from shares_category_mapping where symbol=%s and categorycode=%s"
    _args = (symbol, categorycode )
    task = query_single(db_config['local'], _sql, _args)
    
    return task

def query_listcategory(v):
    _sql = "select code from category where source=%s order by code"
    _args = (v)
    tasks = query(db_config['local'], _sql, _args)
    return tasks

def query_symbol(code):
    _sql = "select symbol from shares where code=%s order by code"
    _args = (code)
    tasks = query_single(db_config['local'], _sql, _args)
    return tasks


# a股份

def runParse(v1,v2):
    clist1 = query_listcategory(v1);
    for i in range(0, len(clist1)):
        getAll(clist1[i]['code'],v2)
     

t1=Thread(target=runParse,args=('thsgn','_gn',))
t1.start()    
t2=Thread(target=runParse,args=('thshy','_hy',))
t2.start()           
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
