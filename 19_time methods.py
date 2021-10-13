import pandas as pd
from datetime import datetime

myyear = 2021
mymonth = 1
myday = 1
myhour = 2
mymin = 30
mysec = 15

mydate = datetime(myyear,myday,mymonth,myhour)
# print(mydate) #2021-01-02 02:00:00

myser = pd.Series(['Nov 3,1990','2000-01-01',None])
print(myser)
'''
0    Nov 3,1990
1    2000-01-01
2          None
'''

#********************Convering Strings to Datetime Object******************
chng_datetime = pd.to_datetime(myser)
print(chng_datetime)
'''
we get,
0   1990-11-03
1   2000-01-01
2          NaT

NOTE : Now we can perform operations such as finding year and date month in string
'''
# print(chng_datetime[0].year) 1990
euro_date = '31-12-2000'
europian_DF = pd.to_datetime(euro_date)
# print(europian_DF)#2000-12-31 00:00:00
#if we want day is first and then month and year
print(pd.to_datetime(euro_date,dayfirst=True))

#cleaning data to proper datetime format
style_date = '12--12--2021'
new_date = pd.to_datetime(style_date,format="%d--%m--%Y")
# print(new_date) 2021-12-12 00:00:00


custom_date = "12th of Dec,2021"
# print(pd.to_datetime(custom_date)) 2021-12-12 00:00:00

sales = pd.read_csv('RetailSales_BeerWineLiquor.csv')
# print(sales)

#if you want access the first element of DATE then use following method(conversion as Datetime object)
sales['DATE'] = pd.to_datetime(sales['DATE'])
# print(sales['DATE'][0]) 1992-01-01 00:00:00
print(sales['DATE'][0].year)#1992

#parse_dates = turns things into real datetime types.
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv',parse_dates=[0])
#sales = sales.set_index('DATE')
#print(sales.resample(rule='A').mean())

#want series of year? here we go...
print(sales['DATE'].dt.year)
print(sales['DATE'].dt.month)