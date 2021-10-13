import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index
'''
- Often DataFrames arenot in the exact same order or format meaning wee can not simply concatenate them together.
- In this case,we need to merge the DataFrames.
- This is analogous to a JOIN command in SQL.

- merge takes in key argument labeled "how".

- 3 ways of mergging tables
1.Inner
2.Outer
3.Left or Right


'''
#********************INNER MERGE*********************
'''
NOTE : table order doesn't matter
'''

registration = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Clarie','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xaiver','Andrew','Yolanda','Bobo']})

print(registration)
print(logins)

#inner merge
print(pd.merge(registration,logins,how='inner',on='name'))
'''
we get,
   reg_id    name  log_id
0       1  Andrew       2
1       2    Bobo       4
'''

#******************LEFT AND RIGHT MERGE*******************
#--------LEFT--------
'''
NOTE : order matters here
- If we put how = 'left' that means merge all values of left table in merge_table irrespective of does second column have value for left's on column or not.
'''
print(pd.merge(registration,logins,how="left",on='name'))
'''
we get,
   reg_id    name  log_id
0       1  Andrew     2.0
1       2    Bobo     4.0
2       3  Clarie     NaN
3       4   David     NaN
'''

#----------RIGHT---------
print(pd.merge(registration,logins,how='right',on='name'))
'''
we get,
   reg_id     name  log_id
0     NaN   Xaiver       1
1     1.0   Andrew       2
2     NaN  Yolanda       3
3     2.0     Bobo       4
'''

'''
NOTE : we can also specifies left= and right= in pd.DataFrame()
'''

#************************OUTTER MERGE**********************
'''
NOTE : order not matter
NOTE : get all data from both table
'''
print(pd.merge(registration,logins,how='outer',on='name'))
'''
we get,
   reg_id     name  log_id
0     1.0   Andrew     2.0
1     2.0     Bobo     4.0
2     3.0   Clarie     NaN
3     4.0    David     NaN
4     NaN   Xaiver     1.0
5     NaN  Yolanda     3.0
'''


#*****joining index instead of columns******
registration = registration.set_index('name')
##### using .reset_index the result will going to as it was.
'''
new registration table with name as index
        reg_id
name
Andrew       1
Bobo         2
Clarie       3
David        4

now merge this registration table with logins table
'''
print(registration)
print(pd.merge(registration,logins,left_index=True,right_on='name'))
'''
we get,
   reg_id  log_id    name
1       1       2  Andrew
3       2       4    Bobo
'''


#chnaging name of registartion name column as reg_name and merge them with login's name column
registration = registration.reset_index()
# print(registration)
#changing name of 'name' to 'reg_name'
registration.columns = ['reg_name','reg_id']
# print(registration)

#*************************************************************************************************
results = pd.merge(registration,logins,left_on='reg_name',right_on='name',how='inner')
'''
we get,
  reg_name  reg_id  log_id    name
0   Andrew       1       2  Andrew
1     Bobo       2       4    Bobo
'''
#**************************************************************************************************
'''
if you want to remove extra column either name/reg_name do this
'''
print(results.drop('reg_name',axis=1))
'''
   reg_id  log_id    name
0       1       2  Andrew
1       2       4    Bobo
'''


