from os import read
import pandas as pd
import numpy as np
'''
Data Frame --> It is a table of columns and rows in pandas that we can easily restructure and filter

Formal Definition --> A group of Pandas Series that share the same index.
'''
np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
#print(mydata)
myindex = ['MH','MP','UP','KA']# index goes with a row
mycolumns = ['Jan','Feb','Mar']
df = pd.DataFrame(index=myindex,data=mydata,columns=mycolumns)
# print(df)
'''
Output :
    Jan  Feb  Mar
MH   95   11   81
MP   70   63   87
UP   75    9   77
KA   40    4   63
'''

# to get information regarding dataframe use .info()
# print(df.info())

'''
Output : 
<class 'pandas.core.frame.DataFrame'>
Index: 4 entries, MH to KA
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Jan     4 non-null      int32
 1   Feb     4 non-null      int32
 2   Mar     4 non-null      int32
dtypes: int32(3)
memory usage: 80.0+ bytes
None
'''

# how to read data from files
#Where is my python code located?
df2 = pd.read_csv('tips.csv')
day = df2.columns[4]
day_col = pd.read_csv('tips.csv').day #prints all data of day columns in console
# count = 0
# for i in day_col:
#     if i == "Thur":
#         count = count+1
# print(count)
# print(day_col)

smoker = df2.columns[3]
smoker_col = pd.read_csv('tips.csv').smoker
count_smoker = 0
for i in smoker_col:
    if i.lower() == 'yes':
        count_smoker += 1
print(count_smoker)
print(smoker_col.count())
total = smoker_col.count()
non_smoker = total - smoker_col.count()
print(f'{round((count_smoker/total)*100,2)}% of People among this data smokes')




