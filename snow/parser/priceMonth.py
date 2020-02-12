import sys
import os
from warnings import catch_warnings
sys.path.append(os.getcwd())
import datetime
 
from threading import Thread
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()

from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog 
no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['month', 'begin', 'high', 'low', 'end', 'volume', 'amount']  
logger = getLog('parser', 'priceMonth');


def insert(year, month):
    # add more args 
    _args = [int(year), int(month)]
    _sql = "Insert into `snow`.`pricemonth` (`year`,`month`,`symbol`,`lastday`,`firstday`,`high`,`low`,`amount`)  SELECT `year`,month(`day`),`symbol`,max(`day`),min(`day`),max(high),max(low),sum(amount)  FROM snow.priceday where `year`=%s and month(`day`)=%s and left(symbol,4) in ( 'SH60', 'SZ20', 'SZ00','SZ39') group by `year`,month(`day`),`symbol`"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def updateEnd(year, month):
    # add more args 
    _args = [int(year), int(month)]
    _sql = "update priceday x, pricemonth y set y.end = x.end where  y.symbol = x.symbol and y.lastday = x.day and y.year = x.year and y.year=%s and y.month=%s"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def updateBegin(year, month):
    _args = [int(year), int(month)]
    _sql = "update priceday x, pricemonth y set y.begin = x.begin where  y.symbol = x.symbol and y.firstday = x.day and y.year = x.year and y.year=%s and y.month=%s"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def updatePE(year, month):
    _args = [ ]
    _sql = "update snow.pricemonth m, mfinancialindex f set m.pe=m.`end`/f.`basiceps`,m.p=100/(m.`end`/f.`basiceps`),m.basiceps=f.basiceps,m.naps=f.naps,m.totassgrowrate=f.totassgrowrate,m.netincgrowrate=f.netincgrowrate,m.mainbusincgrowrate=f.mainbusincgrowrate  where m.symbol = f.symbol and m.year="+str(year)+" and m.month="+str(month)+"  and  date_format((m.year*10000+m.month*100+15),'%%Y-%%m-%%d') between   DATE_ADD(date_format(reportdate,'%%Y-%%m-%%d'),INTERVAL 1 DAY) and DATE_ADD(date_format(reportdate,'%%Y-%%m-%%d'),INTERVAL 3 MONTH)"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def updatecircskamt(year, month):
    _args = [int(year), int(month)]
    _sql = "select  symbol from pricemonth where year=%s and month=%s and totalshare is null"
    tasks = query_single(db_config['local'], _sql, _args)
    l = len(tasks)
    for i in range(0, l):
        r = tasks[i]        
        ks = query_kamt(r['symbol'], year, month)
        if len(ks) > 0:
            k = ks[0]
            _sql2 = "update  pricemonth  set totalshare = %s ,circskamt =%s where symbol = %s and year=%s and month=%s"
            _args2 = [ k['totalshare'], k['circskamt'], r['symbol'], int(year), int(month)]
            insertOrUpdate(db_config['local'], _sql2, _args2)   
           
    return


def query_kamt(symbol, year, month):
    _sql = "SELECT totalshare,circskamt   FROM snow.equity where symbol =%s and  begindate  <= " + str ((year * 10000) + month*100+31) + " order by begindate desc"
    _args = (symbol)
    tasks = query_single(db_config['local'], _sql, _args)
    return tasks


for x in range (2006, 2018):
    for f in range(1, 13):
        updatePE(x, f)

# delete from `snow`.`pricemonth` where `year`=2018
 
 # SELECT m.symbol,m.year,m.month,m.pe,m.p,f.basiceps,m.end FROM snow.pricemonth m, mfinancialindex f where m.symbol = f.symbol and f.symbol in ('SH600000')  and  date_format((m.year*10000+m.month*100+15),'%%Y-%%m-%%d') between   DATE_ADD(date_format(reportdate,'%%Y-%%m-%%d'),INTERVAL 1 DAY) and DATE_ADD(date_format(reportdate,'%%Y-%%m-%%d'),INTERVAL 3 MONTH) order by m.year desc, m.month desc;
