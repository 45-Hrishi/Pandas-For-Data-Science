import pandas as pd
import numpy as np

df = pd.read_csv('mpg.csv')
# print(df)
year_df = df.groupby(['model_year','cylinders']).mean()
# print(year_df)

#************xs --> cross section**************
#key only takes one value
print(year_df.xs(key=70,level='model_year'))


#four_cylinder = year_df.xs(key=4,level='cylinders')
#print(four_cylinder)
print(year_df.xs(key=4,level='cylinders'))#gives model_year as index having 4 cyliniders


#cylinders having value 6 and 8 in it 
cylin68 = df[df['cylinders'].isin([6,8])]
print(cylin68)

#cylinders having value 6 and 8 with model_year with mean except 4
with_model_year = cylin68.groupby(['model_year','cylinders']).mean()
print(with_model_year) 


#*****swapping index levels******
swap = year_df.swaplevel()
print(swap)


#*****Sorting index according to choiceble index******
''' Tip :- always sort by outermost levels '''
sortting_index = year_df.sort_index(level='model_year',ascending=False)
print(sortting_index)


#applying multiple aggregate functions on each column
func_ = df.agg({'mpg':['max','mean'],'weight':['max','mean']})
print(func_)
'''
We Get,
            mpg       weight
max   46.600000  5140.000000
mean  23.514573  2970.424623
'''


