# 香港 每日持股
# 上海，深圳

import sys
import os
from _ssl import txt2obj
sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
import requests
import datetime
from selenium.webdriver.support.ui import Select
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()
import time
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog
ssl._create_default_https_context = ssl._create_unverified_context

 
no_record = 0
not_updated = 0 
not_change = 0
added = 0
fields = ['day', 'market', 'name', 'pholderamt', 'pholderrto']  
logger = getLog('ant','hk_shareholderday');

def getHtml(browser, market, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
        
    folder_path = fs_config['root'] + "/hk_shareholderday2/" + market
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" + timestr + "-nodata.html";  
    
    if  os.path.exists(file) == True :
        logger.info  ("no need to ant exist file :" + file)
        return
    
    
    pnlResult = browser.find_element_by_id("pnlResult")
    ss = str.strip(pnlResult.find_element_by_tag_name("div").text).replace("持股日期: ", "", 7).split('/')
    datestr = ss[2] + "-" + ss[1] + "-" + ss[0]
    file = folder_path + "/" + datestr + ".html";  
    if  os.path.exists(file) == True :
        logger.info  ("no need to ant exist file :" + file)
        return
    table = browser.find_elements_by_class_name("result-table")[0]
    if table == None :
        logger.info  ("no data:" + nodatafile)
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    txt=browser.find_element_by_id("form1").get_attribute('innerHTML')
    f = open(file, 'w') 
    f.write(txt)
    f.close()    
    logger.info  ("write file :" + file)   
    return  

def handlePage(browser,url, market, timestr):
    folder_path = fs_config['root'] + "/hk_shareholderday2/" + market
    file = folder_path + "/" + timestr + ".html";  
    if  os.path.exists(file) == True :
        logger.info  ("no need to ant exist file :" + file)
    else:
        getHtml(browser, market, timestr)
    
    
def handlePages(browser,url, market, timestr):
    browser.get(url) 
    now = time.localtime(time.time())
    try:   
        for m in range (1,2):
            for d in range(0, 30):
                    ddlShareholdingDay= Select( browser.find_element_by_id("ddlShareholdingDay"))
                    ddlShareholdingMonth= Select( browser.find_element_by_id("ddlShareholdingMonth"))
                    ddlShareholdingYear= Select( browser.find_element_by_id("ddlShareholdingYear"))
                    ddlShareholdingYear.select_by_index(0)
                    ddlShareholdingMonth.select_by_index(m)
                    ddlShareholdingDay.select_by_index(d)
                    dd= time.strptime("2018-"+str(m+1)+"-"+str(d+1)+" 23:59:59", '%Y-%m-%d %H:%M:%S')
                    
                    if now <= dd:  
                        return
                    timestr = str(time.strftime('%Y-%m-%d', dd))
                    folder_path = fs_config['root'] + "/hk_shareholderday2/" + market
                    file = folder_path + "/" + timestr + ".html";  
                    if  os.path.exists(file) == True :
                        logger.info  ("no need to ant exist file :" + file)
                    else:
                        browser.find_element_by_id("btnSearch").click()
                        time.sleep(1)
                        handlePage(browser,url, market, timestr)
    
    except Exception as err:
        logger.info  ("exception:")
    
# a股份

browser = webdriver.Firefox()
 
handlePages(browser,"http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=hk" , 'hk', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
handlePages(browser,"http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sz" , 'sz', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
handlePages(browser,"http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh" , 'sh', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
browser.close()
logger.info  ("no_record: %s" % no_record)
logger.info  ("same and not_updated: %s" % not_updated)
logger.info  ("not_change: %s" % not_change)
logger.info  ("added: %s" % added)
