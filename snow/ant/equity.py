#股本变更表
#主要财务指标.json
import sys
import os
from linecache import cache
sys.path.append(os.getcwd())
import ssl
import requests
import json
import pymysql
pymysql.install_as_MySQLdb()
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
import datetime
import time
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog
ssl._create_default_https_context = ssl._create_unverified_context


no_record = 0
not_updated = 0  
not_change = 0
added = 0
         
logger = getLog('ant', 'equity');

 
def getHtml(url, symbol, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
    
    folder_path = fs_config['root'] + "/equity/" + symbol
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" +timestr+  "-nodata.html";  
    if  os.path.exists(file) == True:
        logger.info ("no need to ant exist file :" + file)
        return
    if  os.path.exists(nodatafile) == True:
        logger.info ("no need to ant exist file :" + nodatafile)
        return
    
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session.get('https://xueqiu.com/')
    r = session.get(url)
    logger.info  ("request:" + url)
    time.sleep(0.5)
    txt = r.content.decode('utf-8')
    logger.info  ("request:" + url)    
    j = json.loads(txt)   
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)  
    try:
        if len(j['list']) ==0:
            f = open(nodatafile, 'w')             
            f.write(txt)
            f.close()
            logger.info ("write file :" + nodatafile)
            return
    except Exception as err:  
        f = open(nodatafile, 'w')             
        f.write(txt)
        f.close()
        logger.info ("write file :" + nodatafile)
        return            
    index = j['list'][0];
    if index != None :
        date_time = datetime.datetime.strptime(index['begindate'],'%Y%m%d')
        dstr =  date_time.strftime('%Y-%m-%d')
        file = folder_path + "/" + dstr + ".html";
        if  os.path.exists(file) == True:
            logger.info ("no need to ant exist file :" + file)
            return
        
          
        f = open(file, 'w') 
        f.write(txt)
        f.close()
        logger.info ("write file :" + file)
 
def query_list():
    _sql = "select symbol,code from shares where left(symbol,4) in ('SH60','SH90','SZ00','SZ20','SZ30') order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

 
# a股份
stocklist = query_list()
for i in range(len(stocklist)):
    symbol = stocklist[i]['symbol']
    getHtml("https://xueqiu.com/stock/f10/shareschg.json?symbol="+symbol+"&page=1&size=50&_=1514872821568", symbol, '2018-02-20')
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
