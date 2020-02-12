#主要财务指标.json
import json
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


fields = ['compcode', 'reportdate', 'basiceps', 'naps', 'opercashpershare', 'peropecashpershare', 'weightedroe', 'mainbusincgrowrate', 'netincgrowrate', 'totassgrowrate',
          'salegrossprofitrto','mainbusiincome','mainbusiprofit','totprofit','netprofit','totalassets','totalliab','totsharequi','operrevenue','invnetcashflow','finnetcflow','chgexchgchgs',
          'cashnetr','cashequfinbal' 
          ]  
logger = getLog('parser', 'mfinancialindex');


def getAll(symbol): 
    path = fs_config['root'] + "/mfinancialindex/" + symbol
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if file.rfind('nodata') > 0:
                logger.info('nodata:' + fullpath)
            else:
                dd = int(file.replace(".html", "", 5).replace("-", '', 5))
                dbrs = query_npool(symbol, dd)           
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
    j = json.loads(txt)
    table = j['list'];
    if table != None :
        
        
        for i in range(0, len(table)):              
            stock = table[i];           
            dbrs = query_npool(symbol, stock['reportdate'])     
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
    _sql = "INSERT INTO `snow`.`mfinancialindex` (`symbol`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(symbol, day): 
    _sql = "select *   from mfinancialindex where symbol=%s and reportdate=%s"
    _args = (symbol, day)
    task = query_single(db_config['local'], _sql, _args)
    
    return task



def query_list2():
    _sql = "select distinct left(symbol,6) as k from shares where left(symbol,4) in ('SZ30','SH60','SH90','SH00','SZ00','SZ20','SZ39') "
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks


def query_list(v):
    _sql = "select symbol,code from shares where left(symbol,6) ='"+v+"' order by symbol"
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
