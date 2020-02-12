# snow
A project developed to analyze China's A-share market.  The main functions are crawler and simple report.  The implementation language is Python
# The project is for personal research only and has no commercial purpose.The project will not provide the data collected by the crawler.


 
### Crawler scripts to run every night：  
&emsp;foundsday.py  
&emsp;priceday.py  
&emsp;marginfinancingday.py  
&emsp;hk_shareholderday.py  
### Crawler scripts to run every month, run in weekend：  
&emsp;stockcategorylist.py  
&emsp;stocklist.py  
&emsp;company_info.py  
&emsp;equity.py  
&emsp;mfinancialindex.py  


### Souces:  
股票列表（分页）  
https://xueqiu.com/stock/cata/stocklist.json?page=1&size=30&order=desc&orderby=code&type=11%2C12&_=1514540211629  
公司简介  
https://xueqiu.com/S/SH900957/GSJJ  
https://xueqiu.com/stock/f10/compinfo.json?symbol=SH900957&page=1&size=4&_=1514540425265   
股本结构变动（分页）    
https://xueqiu.com/S/SH900957/GBJG    
https://xueqiu.com/stock/f10/shareschg.json?symbol=SH900957&page=1&size=4&_=1514541355898    
主要股东  
https://xueqiu.com/S/SH900957/ZYGD   
https://xueqiu.com/stock/f10/shareholder.json?symbol=SH900957&page=1&size=4&_=1514541531757  
流通股东  
https://xueqiu.com/S/SH900957/LTGD   
https://xueqiu.com/stock/f10/otsholder.json?symbol=SH900957&page=1&size=4&_=1514541872755  
股东户数(分页)  
https://xueqiu.com/S/SH900957/GDHS  
https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH900957&page=1&size=4&_=1514541954483  
分红送配(分页)    
https://xueqiu.com/S/SH900957/FHPS    
https://xueqiu.com/stock/f10/bonus.json?symbol=SH900957&page=1&size=4&_=1514542039344    
主要财务指标(分页)    
https://xueqiu.com/S/SZ002576/ZYCWZB   
https://xueqiu.com/stock/f10/finmainindex.json?symbol=SZ002576&page=1&size=4&_=1514872821568  
综合损益表(分页)
https://xueqiu.com/S/SZ002576/GSLRB
https://xueqiu.com/stock/f10/incstatement.json?symbol=SZ002576&page=1&size=4&_=1514874192123  
资产负债表(分页)  
https://xueqiu.com/S/SZ002576/ZCFZB  
https://xueqiu.com/stock/f10/balsheet.json?symbol=SZ002576&page=1&size=4&_=1514875090490  
现金流量表(分页)  
https://xueqiu.com/S/SZ002576/XJLLB  
https://xueqiu.com/stock/f10/cfstatement.json?symbol=SZ002576&page=1&size=4&_=1514883381056    
历史交易  
http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/000858.phtml?year=2016&jidu=2  
    
融资融券  
http://data.10jqka.com.cn/market/rzrqgg/code/601318/  
http://data.10jqka.com.cn/market/rzrqgg/code/601318/order/desc/page/1/ajax/1/  
业绩预告  
http://data.10jqka.com.cn/financial/yjyg/  
http://data.10jqka.com.cn/financial/yjyg/date/2017-06-30/ajax/1/  
限售解禁  
http://data.10jqka.com.cn/market/xsjj/  
资金流向  
http://stockpage.10jqka.com.cn/600802/funds/#funds_lszjsj  
行业分类   
http://q.10jqka.com.cn/thshy/detail/code/881112/    

### All data store in Mysql. you can see table scheme in db/table/snow_cashflow.sql
