from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np

df = pd.read_csv('mpg.csv')
# print(df)
print(df['model_year'].unique())#[70 71 72 73 74 75 76 77 78 79 80 81 82]
print(df['model_year'].value_counts())#returns count of unique column values

print(df.groupby('model_year').mean())

#if we want to groupby any column with any function then use following method
print(df.groupby('model_year').mean()['mpg']) 
#prints only mean of mpg column

#groupby multiple columns
print(df.groupby(['model_year','cylinders']).mean())

#getting index of dataframe
year_df = df.groupby(['model_year','cylinders']).mean()
print(year_df.index.names) #prints ----> ['model_year', 'cylinders']

#getting index levels
print(year_df.index.levels)#prints -----> [[70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [3, 4, 5, 6, 8]]
#first list for 'model_year' and second list for 'cylinders'

#getting values for outside level index
print(year_df.loc[70])#prints -----> dataframe of values comes under '70' index
print(year_df.loc[[70,82]])#prints -----> dataframe of values comes under '70' and '80' index

#getting values under index1 and index2
print(year_df.loc[(70,4)])
'''
mpg               25.285714
displacement     107.000000
weight          2292.571429
acceleration      16.000000
origin             2.285714
'''







