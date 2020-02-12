# 每日价格，新浪

import sys
import os
from warnings import catch_warnings
sys.path.append(os.getcwd())

import ssl
import requests
import json
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()
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
fields = ['day', 'begin', 'high', 'low', 'end', 'volume', 'amount']  
logger = getLog('ant', 'priceday');

def getHtml(url, symbol, foucs, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
    folder_path = fs_config['root'] + "/priceday/" + symbol
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" + timestr + "-nodata.html";  
    if  os.path.exists(file) == True :
        logger.info ("no need to ant exist file :" + file)
        return
    if  os.path.exists(nodatafile) == True and foucs == False:
        logger.info ("no need to ant exist file :" + file)
        return
    time.sleep(2)
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # session.get('http://vip.stock.finance.sina.com.cn/')
    txt = ''   
    try:  
        r = session.get(url)
        txt = r.content.decode('gbk')
    except Exception as err:  
        try:  
            time.sleep(3)
            r = session.get(url)
            txt = r.content.decode('gbk')
        except Exception as err:  
            try:  
                time.sleep(5)
                r = session.get(url)
                txt = r.content.decode('gbk')
            except Exception as err:
                time.sleep(9)
                r = session.get(url)
                txt = r.content.decode('gbk')
    logger.info  ("request:" + url)            
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    html = BeautifulSoup(txt, 'html.parser')
    table = html.find("table", attrs={'id': 'FundHoldSharesTable'})
    if table == None :
        f = open(nodatafile, 'w') 
        f.write(txt)
        f.close()
        return    
         
    f = open(file, 'w') 
    f.write(txt)
    f.close()
    logger.info ("write file :" + file)
    return  
   

def query_npool(symbol, day): 
    _sql = "select *   from priceday where symbol=%s and day=%s"
    _args = (symbol, day)
    task = query_single(db_config['local'], _sql, _args)
    
    return task

#
def query_list():
    _sql = "select symbol,code from shares where left(symbol,4) in ('SZ30','SH60','SH90','SZ00','SZ20','SZ39') order by symbol"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks

 
# a股份
stocklist = query_list()
# 
for i in range(0, len(stocklist)):
    symbol = stocklist[i]['symbol']
    code = stocklist[i]['code']
    logger.info ("" + str(i))
 #   for x1 in range(2017, 2018):
  #      for x2 in range(1, 5):
  #          getHtml("http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/" + code + ".phtml?year=" + str(x1) + "&jidu=" + str(x2), symbol, False, str(x1) + "-" + str(x2) + "S")
         
    getHtml("http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/" + code + ".phtml",symbol, True,  str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
  
 
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
