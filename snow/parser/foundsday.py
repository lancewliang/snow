# 每日资金流入流出，同花顺
import datetime
import sys
import os
sys.path.append(os.getcwd())
import ssl
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog
ssl._create_default_https_context = ssl._create_unverified_context
from threading import Thread
no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['day', 'amount', 'larger', 'med', 'small']  

logger = getLog('parser', 'foundsday');


def getAll(symbol): 
    path = fs_config['root'] + "/foundsday/" + symbol
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if file.rfind('nodata') > 0:
                logger.info('nodata:' + fullpath)
            else:
                dd = int(file.replace(".html", "", 5).replace("-", '', 5))
                date_time = datetime.datetime.strptime(str(dd),'%Y%m%d')
                year =  date_time.strftime('%Y')
                
                maxdayrs=query_Maxnpool(symbol,year)
                mday = 0
                try:
                    mday = int(maxdayrs[0]['mday'])
                except:
                    mday = 0
                if  mday>=dd :
                    logger.info("symbol: "+symbol+" more than date maxday:" + str(mday))
                else:    
                    dbrs = query_npool(symbol, dd,year)           
                    if len(dbrs) == 0:
                        getHtml(symbol, fullpath)

            
def getHtml(symbol, fullpath): 
    global no_record
    global not_updated
    global not_change
    global added
    logger.info('load file:' + fullpath)
    fd = open(fullpath, 'r') 
    txt = fd.read() 
    html = BeautifulSoup(txt, 'html.parser')
    table = html.find("table", attrs={'class': 'm_table_3'})
    if table != None :
        
        trs = table.find_all('tr')
        for i in range(2, len(trs)):  
            tds = trs[i].findAll('td')
            stock = {'day':int(tds[0].text.replace("-", '', 10)), 'amount':float(tds[3].text) , 'larger':float(tds[5].text), 'med':float(tds[7].text), 'small':float(tds[9].text) }
            date_time = datetime.datetime.strptime(str(stock['day']),'%Y%m%d')
            year =  date_time.strftime('%Y')
            dbrs = query_npool(symbol, stock['day'],year)     
 
            if len(dbrs) == 0:
                    insert(stock, symbol,year)
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
    return  

 
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


def insert(record, symbol,year):
    # add more args 
    _args = [symbol,int(year)]
    global fields
    for f in fields:
        _args.append(record[f])
    _sql = "INSERT INTO `snow`.`foundsday` (`symbol`,`year`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s,%s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return

def query_Maxnpool(symbol,  year): 
    _sql = "select max(day) as mday from foundsday partition(p"+year+") where symbol=%s  and year=%s"
    _args = (symbol,   int(year))
    task = query_single(db_config['local'], _sql, _args)
    
    return task


def query_npool(symbol, day,year): 
    _sql = "select * from foundsday partition(p"+year+") where symbol=%s and day=%s and year=%s"
    _args = (symbol, day, int(year))
    task = query_single(db_config['local'], _sql, _args)
    
    return task


def query_list(v):
    _sql = "select symbol,code from shares where left(symbol,6) ='"+v+"' order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

def query_list2():
    _sql = "select distinct left(symbol,6) as k from shares where left(symbol,4) in ('SZ30','SH60','SH90','SH00','SZ00','SZ20','SZ39') "
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

def runParse(v):
    # a股份
    stocklist = query_list(v)
    #
    for i in range(0, len(stocklist)):
        symbol = stocklist[i]['symbol']
        code = stocklist[i]['code']
        #gethistory(symbol)
        getAll(symbol)
     
 
  
stockkeylist = query_list2();
for i in range(0, len(stockkeylist)):
    t1=Thread(target=runParse,args=(stockkeylist[i]['k'],))
    t1.start() 
     
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
