 
import pandas as pd  
import pymysql  
import sys  
import openpyxl
import numpy as np

#SELECT  (m.year*100+m.month),m.end,m.pe,m.p*100,f.basiceps,f.naps,f.totassgrowrate,f.netincgrowrate,f.mainbusincgrowrate  FROM snow.pricemonth m, mfinancialindex f where m.symbol = f.symbol and f.symbol in ('SH600104')  and  date_format((m.year*10000+m.month*100+15),'%Y-%m-%d') between   DATE_ADD(date_format(reportdate,'%Y-%m-%d'),INTERVAL 1 DAY) and DATE_ADD(date_format(reportdate,'%Y-%m-%d'),INTERVAL 3 MONTH) order by m.year desc, m.month desc;



def read_mysql_and_insert():  
      
    try:  
        conn = pymysql.connect(host='localhost',user='root',password='111111',db='snow',charset='utf8')  
    except pymysql.err.OperationalError as e:  
        print('Error is '+str(e))  
        sys.exit()  
        
    try:     
        #sql = "select  symbol,end as E200601 from pricemonth where year=2006 and month=1 order by symbol"  
        sql = "select  symbol,year*100+month as month,end  from pricemonth where left(symbol,4) in ('SZ30','SH60' ,'SZ00' ) and month =12 order by year,month,symbol"
        df = pd.read_sql(sql, con=conn)   
      
    except pymysql.err.ProgrammingError as e:  
        print('Error is '+str(e))  
        sys.exit()   
    df.set_index(['symbol','month' ],inplace=True)  
    t1=df.unstack(level=1)  
   
    #print(t1  )     
    t1= t1.dropna(thresh=7)
     
    t1.to_csv('priceyear.csv',index=True,sep=",")  
   
    
    conn.close()  
     
    print('ok')  
    
def read_name():     
    try:  
        conn = pymysql.connect(host='localhost',user='root',password='111111',db='snow',charset='utf8')  
    except pymysql.err.OperationalError as e:  
        print('Error is '+str(e))  
        sys.exit()   
    df = pd.read_csv("priceyear.csv" )
    df= df.dropna(thresh=7)
    df.rename(columns={'month': 'symbol'},inplace=True)
    df.set_index('symbol' , inplace=False) 
    sql2= "select symbol,name from shares where left(symbol,4) in ('SZ30','SH60' ,'SZ00' )  order by symbol"
    df2 = pd.read_sql(sql2, con=conn)
    df2.set_index('symbol' , inplace=False) 
    df = pd.merge( df2,df, on='symbol') 
    df = df.set_index('symbol', inplace=False ) 
    df.to_csv('priceyear2.csv',index=True,sep=",")  
    conn.close()  
    return
   
#生成年价格表格


def judgeLevel(df):
    
    l = len(df)
    y =0 
    for i in range(2,l-1):
        
        #print( df[0]+":" +str(df[i]) +":"+str(df[i+1]))
        if df[i+1] == None:
            df[i+1] = df[i]
        if df[i+1] == '':
            df[i+1] = df[i]
        x = float(df[i+1])-float(df[i]) 
        if x>0 :
            y= float(df[i+1])/float(df[i])       
        elif x ==0:
            continue               
        else :
            y=y-1
    return y

def handleyear():
    
    df = pd.read_csv("priceyear2.csv")
    df = df.set_index('symbol', inplace=False ) 
    df['level'] = '' # add a column  
    df['level'] = df.apply(lambda r: judgeLevel(r), axis=1)
    df=df[df['level']>0]
    df= df.sort_values(by='level')
    df.to_csv('priceyear3.csv',index=True,sep=",")  


#read_mysql_and_insert()   
#read_name() 
handleyear()      