# 香港 每日持股
# 上海，深圳

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
fields = ['day', 'market', 'name', 'pholderamt', 'pholderrto']  

logger = getLog('parser', 'hk_shareholderday');


def getAll(market): 
    path = fs_config['root'] + "/hk_shareholderday2/" + market
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            dd = int(file.replace(".html", "", 5).replace("-", '', 5))
            dbrs = query_count(dd, market)           
            if int(dbrs[0]['count']) == 0:
                getHtml(market, fullpath)
            else:
                logger.info('ignore file:' + fullpath)

                
def getHtml(market, fullpath): 
    global no_record
    global not_updated
    global not_change
    global added
    
    logger.info('load file:' + fullpath)
    fd = open(fullpath, 'r') 
    txt = fd.read() 
     
    html = BeautifulSoup(txt, 'html.parser')
    
    pnlResult = html.find("div", attrs={'id': 'pnlResult'})
    if pnlResult == None:
        print(html)
        return
    ss = str.strip(pnlResult.find_all('div')[0].text).replace("持股日期: ", "", 7).split('/')
    datestr = ss[2] + ss[1] + ss[0]
    table = html.find("table", attrs={'class': 'result-table'})
    if table != None :
      
        trs = table.find_all('tr')
        for i in range(2, len(trs)):  
            tds = trs[i].findAll('td')
            symbol = str.strip(tds[0].text)
            stock = {'day':int(datestr), 'market':market, 'name': str.strip(tds[1].text) , 'pholderamt':parseNumberstr(tds[2].text), 'pholderrto':parseNumberstr(tds[3].text)}
           
            dbrs = query_npool(symbol, stock['day'], stock['market'])     
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


def parseNumberstr(ss):
    sx = str.strip(ss).replace(',', '').replace('%', '')
    if sx == '':
        return 0
    return float(sx)
    
 
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
    _sql = "INSERT INTO `snow`.`hk_sharedholderday` (`symbol`"
    for f in fields:
        _sql += "," + f;
    _sql += ")VALUES( %s"
    for f in fields:
        _sql += ",%s";
    _sql += ")"
    insertOrUpdate(db_config['local'], _sql, _args)   
    return


def query_npool(symbol, day, market): 
    _sql = "select * from hk_sharedholderday where symbol=%s and day=%s and market=%s"
    _args = (symbol, day, market)
    task = query_single(db_config['local'], _sql, _args)
    
    return task


def query_count(day, market): 
    _sql = "select count(*) as count from hk_sharedholderday where day=%s and market=%s"
    _args = (day, market)
    task = query_single(db_config['local'], _sql, _args)
    
    return task
# a股份


getAll('hk')
getAll('sz')
getAll('sh')
        
logger.info ("no_record: %s" % no_record)
logger.info ("same and not_updated: %s" % not_updated)
logger.info ("not_change: %s" % not_change)
logger.info ("added: %s" % added)
