# 香港 每日持股
# 上海，深圳

import sys
import os
sys.path.append(os.getcwd())

import ssl
import requests

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

def getHtml(url, market, timestr): 
    global no_record
    global not_updated
    global not_change
    global added
        
    folder_path = fs_config['root'] + "/hk_shareholderday/" + market
    file = folder_path + "/" + timestr + ".html";  
    nodatafile = folder_path + "/" + timestr + "-nodata.html";  
    
    if  os.path.exists(file) == True :
        logger.info  ("no need to ant exist file :" + file)
        return
    
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    d = {

#         '__VIEWSTATEGENERATOR':'EC4ACD6F',
#         '__EVENTVALIDATION':'zyo99q/2QiPiGQ/1OvVFw1JawPhdyLdoZ/VsvYrqay7nCBou88Sa4FGXe25TFMCBhSRWflr6c/mW8igFrGgoU0SpzYnWzCh/6IwQpwulBC02Bg+ZUQ5mFRytQDkNu6PeCzNzJMGw18eBIKx07K6IEWsF6Og5J/hAXgiwFeiF58R1LE0l3jAHeuTzLjJ7oSErhkkYvWOmN2CpgqMQyqIzlGLfzYbw8TqQ+6SyQB5vknbPFVpuKVdJ7dzd5DbeaqfWQAyUnB4wZCNue5FPDL+3DIsCvxOZCSHLCRbt043XSs39TzjJ6dRmTB1eoHdqgmzFVH9yZQObrglUeiDB4fe3duoZtShewxup09WBMr2toHCOSJHnb0hJjBtHI+xf61THOpEgxwRBDqgc+dEgm08ZHrj4Mmfm2o7JUandQudqRurY392Gcl49vO92Z7sKZibrfbfeK2B3EJpeIcpsUJSASl7u7js3JnsDHPEN5r4w4UbYmW11q+yOpNgCN5h5WORSG+KpWYlSdGgn818SSmN9btpBxSQVjOen3ZpXpL3ivwxXkWcUjHifZ4i/8uN7s1YwsUoLIzyHmr7ZuD0t4mwbzu3NdkmL4l7M3aMJ5BT+/L/+x/FZ/j+htaSY/gAa/lp7Ep3q6LxoWc7ozY+Qr1AO8WAhqXEuhia381ngjJ+V0+xfkt6k7ZftWLcQqccX9xRxLYnOE3aLlG+K5zV+PX8mWoeSrx0Arozal2h03u1TtnNEwxWRe+P/W4SqSiRqei+rs/hxhkVDM8zMD3bkGgU+kDyYRfJzTVdi8xQNwPCq+1nx3ILhELUNRunSI0nrG/654gn5H5EjvsSZ6i9TGzuCDj8WGo2WLRxwh5bU5G0MUU2phUoZQ0P3vi8jVF0mBPU12Ti0GytX+sacYbFgBEmt/xsx935IbBISShiDx2Ib9YwzrxntGbCIFiztI77LLc2obQG1/dBgopaIhlPF0rIKs+A/m7k8FVPaEINsLOGaAydM2R9N0+i1xoIrMlwIu1pMLEEQo4q33C/1yc2XoG2IVlqevx3viWvQB5ZRgU/PbUaxiLBXH2t6CNWh6cliNJYb/eQ+hDd8kzib2pj7LTnvcPOjRbcEOSWX6JsOp6WDA8cqLiV3BVkg6x0ZWCyosa+ND/OVNgAYPKqY/cD/kVZ29dCdOzk=',
#         '__VIEWSTATE':'5eS8MvbPwcx7GZ5KhjXUWRSVWBX5jSpu617Ds+S+PpLkiyoT7XSHh8Bok8Yc3ZTswUIG9OUBthAi1ytoewRt75eWazgFJ9ztXAe5H+wwxXqloi62nUvz9GD48Blhxx5x5vhtPHfNyZQa+3/Q8ZhP8jcPQO3xppi5piDPl8FQZ7U9irZ8Qh8cmAYvIl3pMZznnPaCxg==',
#         'today': '20180128', 'sortBy': '', 'alertMsg':'', 'ddlShareholdingDay':'23'      , 'ddlShareholdingMonth':'01',
#             'ddlShareholdingYear':'2018', 'btnSearch.x':'24', 'btnSearch.y':'4'
         }
     
    r = session.get(url, data=d)
    txt = r.content.decode('utf-8')
    logger.info  ("request:" + url)
    html = BeautifulSoup(txt, 'html.parser')
    
    pnlResult = html.find("div", attrs={'id': 'pnlResult'})
    ss = str.strip(pnlResult.find_all('div')[0].text).replace("持股日期: ", "", 7).split('/')
    datestr = ss[2] + "-" + ss[1] + "-" + ss[0]
    file = folder_path + "/" + datestr + ".html";  
    if  os.path.exists(file) == True :
        logger.info  ("no need to ant exist file :" + file)
        return
    table = html.find("table", attrs={'class': 'result-table'})
    if table == None :
        logger.info  ("no data:" + nodatafile)
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)
    f = open(file, 'w') 
    f.write(txt)
    f.close()    
    logger.info  ("write file :" + file)   
    return  
 
# a股份


getHtml("http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=hk" , 'hk', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
getHtml("http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sz" , 'sz', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
getHtml("http://sc.hkexnews.hk/TuniS/www.hkexnews.hk/sdw/search/mutualmarket_c.aspx?t=sh" , 'sh', str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
        
logger.info  ("no_record: %s" % no_record)
logger.info  ("same and not_updated: %s" % not_updated)
logger.info  ("not_change: %s" % not_change)
logger.info  ("added: %s" % added)
