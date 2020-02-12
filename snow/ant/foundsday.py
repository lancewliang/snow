# 每日资金流入流出，同花顺

import sys
import os
sys.path.append(os.getcwd())
import ssl
import requests
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()
import time
from PyMysqlPool.db_util.mysql_util import query
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
ssl._create_default_https_context = ssl._create_unverified_context
from snow.config.Mylog import getLog

no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['day', 'amount', 'larger', 'med', 'small']  

logger = getLog('ant', 'foundsday');


def getHtml(url, symbol, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
    
    folder_path = fs_config['root'] + "/foundsday/" + symbol
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" + timestr + "-nodata.html";  
    
    if  os.path.exists(file) == True :
        logger.info ("no need to ant exist file :" + file)
        return
    if  os.path.exists(nodatafile) == True :
        logger.info ("no need to ant exist file :" + nodatafile)
        return
    
    session = requests.Session()
    
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # session.get('http://vip.stock.finance.sina.com.cn/')
    r = session.get(url)
    time.sleep(0.5)
    txt = r.content.decode('utf-8')
    logger.info  ("request:" + url)
    html = BeautifulSoup(txt, 'html.parser')
    table = html.find("table", attrs={'class': 'm_table_3'})
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    if table == None :
        logger.info ("no data:" + nodatafile)
        f = open(nodatafile, 'w') 
        f.write(txt)
        f.close()        
        return        

    f = open(file, 'w') 
    f.write(txt)
    f.close()    
    logger.info ("write file :" + file)   
    return  


def query_list():
    _sql = "select symbol,code from shares where left(symbol,4) in ('SH60','SH90','SH00','SZ00','SZ20','SZ30') order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

 
# a股份
stocklist = query_list()
# 
for i in range(0, len(stocklist)):
    symbol = stocklist[i]['symbol']
    code = stocklist[i]['code'] 
    getHtml("http://stockpage.10jqka.com.cn/" + code + "/funds/" , symbol, str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
    
     
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
