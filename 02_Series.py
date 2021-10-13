import numpy as np
import pandas as pd

# print(pd.Series())
myindex = ['India','Bangaldesh','Pakistan']
mydata = [1947,1971,1947]
myser = pd.Series(data=mydata,index=myindex)
print(myser)

'''
It prints the data frame link below
India         1947
Bangaldesh    1971
Pakistan      1947
dtype: int64
'''

#bydefault means if we don't pass index argument then it will create its own index 
# myser = pd.Series(data=mydata)
# print(myser)

'''
By Default ---> It will how index as (0 1 2.....)
0    1947
1    1971
2    1947
dtype: int64
'''
# print(myser[0]) ---> 1947
# print(myser['India'])  prints ---> 1947

ages = {'Hrishi':19,'Raj':20,'Shubham':21}
print(pd.Series(ages))
'''
By default makes key as index 

Hrishi     19
Raj        20
Shubham    21
dtype: int64
'''
