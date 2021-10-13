import pandas as pd
import numpy as np
import os

#For reading files ---> pd.read_(file_type)
#For writing files ---> df.to_(file_type)
print("Current Working Directory -- >",os.getcwd())


#---------------reading CSV files------------------
'''df = pd.read_csv('example.csv',header=None)
# print(df)
df.to_csv('examples.csv')#this create new csv file'''

#---------------reading HTML tables----------------
'''url = "https://en.wikipedia.org/wiki/World_population"
tables = pd.read_html(url)
# print(tables)#prints all html tables from wikipedia
print(len(tables))#26
world_top10 = tables[0]
print((world_top10['World population (millions, UN estimates)[14]']).drop(11,axis = 0))
# world_top10 = world_top10.drop('#',axis=1)
print(world_top10.columns)
tables = tables[6].set_index('Rank')
print(tables['Population trend'])

print(tables.to_html('smaple_table.html',index = False))'''

#--------------Input and Output in Excel sprreadsheet---------------------

#Pandas treat Excel shreadsheets as dictionary,with key being the sheet name and the value being the dataframe representing the sheet itself
df = pd.read_excel('my_excel_file.xlsx',sheet_name='First_Sheet')
print(df)

#If you don't know the sheetnames then firstly extract all sheetnames list using below code
wb = pd.ExcelFile('my_excel_file.xlsx')
print(wb.sheet_names) #get all sheetnames list

excel_sheet_dict = pd.read_excel('my_excel_file.xlsx',sheet_name=None)
print(type(excel_sheet_dict))#<class 'dict'>
keys = excel_sheet_dict.keys()
values = excel_sheet_dict.values()
print("Keys:",keys,"\nValues:",values)
our_df = excel_sheet_dict['First_Sheet']
our_df.to_excel('example.xlsx',index=False)
print(our_df)


#------------------Pandas Input and Output SQL Databases-----------------
#Creating Temporary database comp RAM
from sqlalchemy import create_engine
temp_db = create_engine('sqlite:///:memory:')
df = pd.DataFrame(data=np.random.randint(low=0,high=100,size=(4,4)),columns=['a','b','c','d'])
print(df)
'''
    a  b   c   d
0  32  39  37  31
1  69  74  13  52
2  10  56  80  27
3  87   3  30   7
'''
df.to_sql(name='new_table',con=temp_db,if_exists="fail")
#If we run it twice then it throws a valuerror 
new_df = pd.read_sql(sql='new_table',con=temp_db)
print(new_df)
'''
It has index new parameter
   index   a   b   c   d
0      0  55  65  29  28
1      1  81  43  90  51
2      2  87  76  17  37
3      3  47  24  71  75
'''

#Selecting only column a.c using SQL syntax
result = pd.read_sql_query(sql='SELECT a,c FROM new_table',con=temp_db)
print(result)
'''
    a   c
0  77  57
1  15  80
2  81  16
3  83  62
'''


