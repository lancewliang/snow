# 每日融資融券余額_同花順

import sys
import os
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

fields = ['day', 'financingsurplus', 'financingbuy', 'financingpaying', 'netfinancingbuy', 'marginsurplus', 'marginsell', 'marginpaying', 'netmarginsell', 'surplus']  

logger = getLog('ant', 'marginfinancingday');


def getHtml(url, symbol, foucs, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
    folder_path = fs_config['root'] + "/marginfinancingday/" + symbol
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" + timestr + "-nodata.html";  
    if  os.path.exists(file) == True :
        logger.info ("no need to ant exist file :" + file)
        return
    if  os.path.exists(nodatafile) == True and foucs == False:
        logger.info ("no need to ant exist file :" + file)
        return
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # session.get('http://vip.stock.finance.sina.com.cn/')
    r = session.get(url)
    time.sleep(1)
    txt = r.content.decode('gbk')
    logger.info  ("request:" + url)
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    html = BeautifulSoup(txt, 'html.parser')
    table = html.find("table", attrs={'class': 'm-table'})
    if table == None :
        f = open(nodatafile, 'w') 
        f.write(txt)
        f.close()
        logger.info ("write file :" + nodatafile)
        return    
    trs = table.find_all('tr')
    for i in range(2, len(trs)):  
        tds = trs[i].findAll('td')
        daystr = tds[1].text.replace("-", '', 10).replace("\n", '', 10);
        if daystr == '':
            f = open(nodatafile, 'w')             
            f.write(txt)
            f.close()
            logger.info ("write file :" + nodatafile)
            return      
    f = open(file, 'w') 
    f.write(txt)
    f.close()
    logger.info ("write file :" + file)
    return  


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
    logger.info ("" + str(i))
#    for x1 in range(1, 22): 
#       getHtml("http://data.10jqka.com.cn/market/rzrqgg/code/" + code + "/order/desc/page/" + str(x1) + "/ajax/1/", symbol, False, str(x1) + "S")
       # time.sleep(1)
    getHtml("http://data.10jqka.com.cn/market/rzrqgg/code/" + code + "/order/desc/page/1/ajax/1/", symbol, True, str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
 
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
 
