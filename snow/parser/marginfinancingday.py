# 每日融資融券余額_同花順

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

no_record = 0
not_updated = 0 
not_change = 0
added = 0

fields = ['day', 'financingsurplus', 'financingbuy', 'financingpaying', 'netfinancingbuy', 'marginsurplus', 'marginsell', 'marginpaying', 'netmarginsell', 'surplus']  

logger = getLog('parser', 'marginfinancingday');


def gethistory(symbol): 
    path = fs_config['root'] + "/marginfinancingday/" + symbol
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            
            if file.rfind('nodata') > 0:
                logger.info('nodata:' + fullpath)
            else:
                if file.rfind('S') > 0: 
                    getHtml(symbol, fullpath)
                        
                        
def getAll(symbol): 
    path = fs_config['root'] + "/marginfinancingday/" + symbol
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            
            if file.rfind('nodata') > 0:
                logger.info('nodata:' + fullpath)
            else:
                if file.rfind('S') > 0: 
                    logger.info('history ignore:' + fullpath)
                else:
                    dd = int(file.replace(".html", "", 5).replace("-", '', 5))
                    dbrs = query_count(dd)                                                  
                    if int(dbrs[0]['count']) == 0:
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
    table = html.find("table", attrs={'class': 'm-table'})
    if table != None :
        
        trs = table.find_all('tr')
        for i in range(2, len(trs)):  
            tds = trs[i].findAll('td')
            daystr = tds[1].text.replace("-", '', 10).replace("\n", '', 10);
            
            if daystr == '':
                no_record = no_record + 1
                return 
            stock = {'day':int(daystr),
                     'financingsurplus':parsenumberstr(tds[2].text) , 'financingbuy':parsenumberstr(tds[3].text),
                     'financingpaying':parsenumberstr(tds[4].text), 'netfinancingbuy':parsenumberstr(tds[5].text),
                     'marginsurplus':float(tds[6].text), 'marginsell':float(tds[7].text),
                     'marginpaying':float(tds[8].text), 'netmarginsell':float(tds[9].text),
                     'surplus':parsenumberstr(tds[10].text)}
           
            dbrs = query_npool(symbol, stock['day'])     
            if len(dbrs) == 0:
                    insert(stock, symbol)
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


def parsenumberstr(ss):
    if ss.rfind('亿') > 0:
        return  round(float(ss.replace("亿", '', 10)) * 100000000, 1)
    if ss.rfind('万') > 0:
        return  round(float(ss.replace("万", '', 10)) * 10000, 1)
    return  float(ss)  
    
 
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


def insert(record, symbol):
    # add more args 
    _args = [symbol]
    global fields
    for f in fields:
        _args.append(record[f])
    _sql = "INSERT INTO `snow`.`marginfinancingday` (`symbol`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(symbol, day): 
    _sql = "select *   from marginfinancingday where symbol=%s and day=%s"
    _args = (symbol, day)
    task = query_single(db_config['local'], _sql, _args)
    
    return task


def query_count(day): 
    _sql = "select count(*) as count from marginfinancingday where day=%s "
    _args = (day)
    task = query_single(db_config['local'], _sql, _args)
    
    return task
# a股份


def query_list():
    _sql = "select symbol,code from shares where left(symbol,4) in ('SH60','SH90','SH00','SZ00','SZ20','SZ30','SZ39') order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

 
# a股份
stocklist = query_list()
# 
for i in range(0, len(stocklist)):
    symbol = stocklist[i]['symbol']
    code = stocklist[i]['code']
    #gethistory(symbol)
    getAll(symbol)
 
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
 
