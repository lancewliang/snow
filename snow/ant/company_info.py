import sys
import os
sys.path.append(os.getcwd())
import ssl
import requests
import json
import pymysql
import time
pymysql.install_as_MySQLdb()

from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config

ssl._create_default_https_context = ssl._create_unverified_context
from snow.config.Mylog import getLog
no_record = 0
not_updated = 0  
not_change = 0
added = 0
fields = ['compname', 'engname', 'founddate', 'regcapital', 'chairman', 'manager', 'legrep', 'bsecretary', 'bizscope', 'compintro']  
logger = getLog('ant', 'company_info');


def getHtml(url, symbol): 
    global no_record
    global not_updated
    global not_change
    global added
    
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session.get('https://xueqiu.com/')
    r = session.get(url)
    txt = r.text 
    logger.info  ("request:" + url)
    j = json.loads(txt)
    stock = j['tqCompInfo'];
    if stock != None:         
            dbrs = query_npool(symbol)     
            if len(dbrs) == 0:
                insert(stock, symbol)
                added = added + 1  
            else:
                if isSame(dbrs[0], stock) == False:
                    logger.info ("<!------------------------ant from: " + url)
                    logger.info (txt)                  
                    logger.info (dbrs[0])
                    logger.info ("database record end ------------need check----------------> ")
                    not_change = not_change + 1
                else:
                    not_updated = not_updated + 1  
    else:
        logger.info('no record:' + url)
        no_record = no_record + 1
    return  

 
def isSame(dbrs, record):
    global fields 
    for f in fields:
        if  str(record[f]) != str(dbrs[f]) :
            return False;
 
    return True;


def insert(record, symbol):
    # add more args 
    _args = [symbol]
    global fields
    for f in fields:
        _args.append(record[f])
    _sql = "INSERT INTO `snow`.`compinfo` (`symbol`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(symbol): 
    _sql = "select *   from compinfo where symbol=%s "
    _args = (symbol)
    task = query_single(db_config['local'], _sql, _args)
    
    return task


def query_list():
    _sql = "select symbol,code from shares where left(symbol,4) in ('SH60','SH90','SH00','SZ00','SZ20','SZ30','SZ39') order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

 
# a股份
stocklist = query_list()
for i in range(len(stocklist)):
    symbol = stocklist[i]['symbol'].decode(encoding="utf-8") 
    getHtml("https://xueqiu.com/stock/f10/compinfo.json?symbol=" + symbol + "&page=1&size=4&_=1514540425265", symbol)
    time.sleep(1)
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
