#類型與股票關係表
import sys
import os
from _ast import Num
sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pymysql

pymysql.install_as_MySQLdb()
import time
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config

from snow.config.Mylog import getLog

logger = getLog('ant', 'stockcategorylist_hy');


def getTableBodyMain(tables):
    l = len(tables)
    for n in range(0, l ):
        try:
            tbody = tables[n].find_element_by_tag_name("tbody")
            if tbody!=None :
                return tables[n]
        except Exception as err:  
            print('')
    return None
    
def handlePage(n,symbol,browser,timestr):
    
    table = browser.find_elements_by_class_name("m-table")    
    folder_path = fs_config['root'] + "/stockcategorylist_hy/" + symbol
    file = folder_path + "/" + timestr +"-"+str(n)+ ".html";   
    if  os.path.exists(file) == True :
        logger.info ("no need to ant exist file :" + file)
        return    
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    
    txt = getTableBodyMain(table).get_attribute('innerHTML')
    f = open(file, 'w') 
    f.write(txt)
    f.close()
    logger.info ("write file :" + file)
    return   
 
def handlePages(symbol,browser,timestr):
    browser.get("http://q.10jqka.com.cn/thshy/detail/code/"+symbol+"/") 
    count=0
    try:
        count =int( str(browser.find_elements_by_class_name("page_info")[0].text).split('/',1)[1]);
    except Exception as err:
        count=1
    print ( str(count))
    for n in range(1, count+1):
        handlePage(n,symbol,browser,timestr)
        if(n<count):
            atags = browser.find_elements_by_class_name("changePage")
            getNodeA(atags,n+1).click()
            time.sleep(1)
           


def getNodeA(nodes, i ):
    l = len(nodes)
    for n in range(0, l ):
        p=nodes[n].get_attribute("page")
        if p == str(i):
            return nodes[n]
    return None               

def query_list():
    _sql = "select code from category where source = 'thshy'"
    _args = ()
    tasks = query(db_config['local'], _sql, _args)
    return tasks



browser = webdriver.Firefox()
stocklist = query_list()
# 
for i in range(0, len(stocklist)):
    code = stocklist[i]['code']
    logger.info ("" + str(i))
    handlePages(code, browser, str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
browser.close()