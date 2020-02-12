import sys
import os
sys.path.append(os.getcwd())
import ssl
import requests
import json
import pymysql
pymysql.install_as_MySQLdb()

from PyMysqlPool.db_util.mysql_util import  query_single, insertOrUpdate
from snow.config.mysql_config import db_config



 
ssl._create_default_https_context = ssl._create_unverified_context
no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['symbol', 'code', 'name']  


def getHtml(url): 
    global no_record
    global not_updated
    global not_change
    global added
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session.get('https://xueqiu.com/')
    r = session.get(url)
    txt = r.text 
       
    j = json.loads(txt)
    stocks = j['stocks'];
    recordSize = len(stocks)
    if recordSize > 0:   
        for stock in stocks:
            dbrs = query_npool(stock)     
            if len(dbrs) == 0:
                insert(stock)
                added = added + 1  
            else:
                if isSame(dbrs[0], stock) == False:
                    print ("<!------------------------ant from: " + url)
                    print (txt)                  
                    print (dbrs[0])
                    print ("database record end ------------need check----------------> ")
                    not_change = not_change + 1
                else:
                    not_updated = not_updated + 1               
    else:
        print('no record:' + url)
        no_record = no_record + 1
    return  

 
def isSame(dbrs, record): 
    global fields
    for f in fields:
        if str(record[f]) != str(dbrs[f]) :
            return False;
 
    return True;


def insert(record):
    # add more args
    _args = []
    global fields
    for f in fields:
        _args.append(record[f])
    _sql = "INSERT INTO shares ("
    for i in range(len(fields)):
        if i > 0 :
            _sql += ",";
        _sql += fields[i];
    _sql += ")VALUES("
    for i in range(len(fields)):
        if i > 0 :
            _sql += ",";
        _sql += "%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(record): 
    _sql = "select *   from shares where symbol=%s "
    _args = (record['symbol'],)
    task = query_single(db_config['local'], _sql, _args)
    return task


# a股份
for i in range(1, 400):
    getHtml("https://xueqiu.com/stock/cata/stocklist.json?page=" + str(i) + "&size=30&order=desc&orderby=code&type=11%2C12&_=1514540211629")

print ("no_record: %s" % no_record)
print ("same and not_updated: %s" % not_updated)
print ("not_change: %s" % not_change)
print ("added: %s" % added)
