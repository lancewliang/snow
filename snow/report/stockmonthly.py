 
import pandas as pd  
import pymysql  
 
import sys
import os
sys.path.append(os.getcwd())
import matplotlib.pyplot as plt
import pymysql
from bs4 import BeautifulSoup
pymysql.install_as_MySQLdb()
from PyMysqlPool.db_util.mysql_util import query, query_single, insertOrUpdate
from snow.config.mysql_config import db_config
from snow.config.fsdata_config import fs_config
from snow.config.Mylog import getLog
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号



def queryone(symbol):
    _sql = "select name from shares where symbol =%s "
    _args = (symbol)
    tasks = query(db_config['local'], _sql, _args)
    return tasks[0]

def querylasttotalshare(symbol):
    sql = "SELECT "
    sql+="(`year` * 100 + `month`) m,  "
    sql+="totalshare "        
    sql+="FROM "
    sql+="snow.pricemonth "
    sql+="WHERE "
    sql+="symbol =%s AND pe IS NOT NULL "
    sql+="ORDER BY year desc , month desc"
    _args = (symbol)
    tasks = query_single(db_config['local'], sql, _args)
    return tasks[0]


def read_mysql(symbol):  
    try:  
        conn = pymysql.connect(host='localhost',user='root',password='111111',db='snow',charset='utf8')  
    except pymysql.err.OperationalError as e:  
        print('Error is '+str(e))  
        sys.exit()  
    stock =  queryone(symbol)  
    lastshare = querylasttotalshare(symbol)  
    try:     
        #sql = "select  symbol,end as E200601 from pricemonth where year=2006 and month=1 order by symbol"  
        sql = "SELECT `year`,"
        sql+="(`year` * 100 + `month`) m, end,"
        sql+="end / ("+str(lastshare['totalshare'])+" / totalshare) end2,"
        sql+="(amount/10000/100000)-100 amount,"
        sql+="pe,"
        sql+="p-100 p,"
        sql+="(basiceps*100)+100 basiceps,"
        sql+="totassgrowrate-100 totassgrowrate,"
        sql+="mainbusincgrowrate-100 mainbusincgrowrate,"
        sql+="(totalshare/10000)-100 t," 
        sql+="circskamt/totalshare*100 c,"       
        sql+="totalshare*end/10000 v "
        sql+="FROM "
        sql+="snow.pricemonth "
        sql+="WHERE "
        sql+="symbol = '"+symbol+"' AND pe IS NOT NULL "
        sql+="ORDER BY year asc , month asc"
        df = pd.read_sql(sql, con=conn)   
      
    except pymysql.err.ProgrammingError as e:  
        print('Error is '+str(e))  
        sys.exit()   
    #df.set_index(['m' ],inplace=True)  
    df.loc[df['pe']>120,'pe']=120
    df.loc[df['pe']<-100,'pe']=-100
    df.loc[df['amount']>500,'amount']=500
    y1=df['end2'].T.values
    
    y2=df['pe'].T.values
    y3=df['p'].T.values
    y4=df['basiceps'].T.values
    y5=df['t'].T.values
    y6=df['end'].T.values
    y7=df['amount'].T.values
    y8=df['mainbusincgrowrate'].T.values
    y9=df['totassgrowrate'].T.values
    y10=df['c'].T.values
    
    x1=range(0,len(y1))
    x2=range(0,len(y2))
    x3=range(0,len(y3))
    x4=range(0,len(y4))
    x5=range(0,len(y5))
    x6=range(0,len(y6))
    x7=range(0,len(y7))
    x8=range(0,len(y8))
    x9=range(0,len(y9))
    x10=range(0,len(y10))
    plt.figure(figsize=(16, 8))
    plt.plot(x1,y1,'',label="前复权价格")
    plt.plot(x2,y2,'',label="市盈率(1/每股收益)")
    plt.plot(x3,y3,'',label="盈利率(1/市盈率) -100為0" )
    plt.plot(x4,y4,'',label="每股收益(分),100為0")
    plt.plot(x5,y5,'',label="市值(亿股),-100為0")
    plt.plot(x6,y6,'',label="月结算价")
    plt.plot(x7,y7,'',label="交易金額(亿),-100為0")
    plt.plot(x8,y8,'',label="主营业务增长率 -100為0")
    plt.plot(x9,y9,'',label="总资产增长率 -100為0")
    plt.plot(x10,y10,'',label="股本流通率")
    plt.title(symbol+" "+stock['name']+'基本面分析')
    plt.legend(loc='upper left')
    yearnum =[]
    yearname=[]
    
    years=[]
    
    for i in range(2006,2019):
       
        l = len( df[df.year.isin([i])])
        if l>0:
            years.append( i )
        
    for i in years:
        yearnum.append((i-years[0])*12)
        yearname.append(str(i))
    
    plt.xticks(yearnum,yearname)
    plt.xlabel('年份')
    plt.ylabel('数值')
    plt.grid(x1)
    plt.show()
    
#SZ000651 海康威视  偏高B
#SZ002415 海康威视  偏高B 
#SH600276 瑞恒医院 偏高A 
#SH601318 中国平安 偏高A
#SH600887 伊利  偏高B
#SH600519 茅台  严重高估
#SH600048 保利地产 偏高C 
#SH600518 康美药业 偏高C
#SZ002008 大足激光 偏高A 
#SZ000538 云南白药 偏高B
#SZ000895 双汇发展 一般
#SZ002049 紫光国兴 偏高B
#SZ000002 万科 偏高B
read_mysql('SH600570')