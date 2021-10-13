import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')
print(df.head())
#**************************Single Conditional Filtering***********************
print(df[df['total_bill']>30])#df['total_bill']>30 --> gives us boolean values and 
#df[boolean_value] fives the dataframe we want.

#**************************Multiple Conditional Filtering*********************
#to check more than one conditional checking we can't use python 'and' operator because 'and' operator only checks two boolean values not exact values.

#to add more than one condition use '&' operator instead
#& - use like and operator
#| - use like or opertaor
print(df[(df['total_bill']>40) & (df['sex'] == 'Male')])

#*************************isin operator********************************
options = ['Sun','Sat']
print(df[df['day'].isin(options)])



