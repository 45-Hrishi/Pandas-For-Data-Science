import pandas as pd
import numpy as np
from pandas.core.series import Series

'''print(np.nan)#prints ---> nan
print(pd.NA)#prints ---> <NA>
print(pd.NaT)#prints ---> NaT

print(np.nan == np.nan)#prints ---> False
#if we want to make them true 
print(np.nan is np.nan)#prints ---> True'''

df = pd.read_csv('movie_scores.csv')
print(df)

#for getting NaN in dataset
print(df.isnull()) #prints ---> true if NaN in dataset

#for getting not NaN in dataset(content in dataset)
print(df.notnull())#prints ----> true if NaN is not there in dataset

print(df[df['pre_movie_score'].notnull()]) #prints the dataset cells having pre_movie_score value.
print(df[df['pre_movie_score'].isnull()]) #prints the dataset cells having pre_movie_score value NaN

print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())]) #prints the dataset cells having pre_movie_score value NaN and first_name value is precent


#keep data
#drop data
#fill data

#keep data
print(df)

#drop data
# print(help(df.dropna))
print(df.dropna()) #drops all NaN value rows
print(df.dropna(thresh=1))#keep row which has grater than thresh not(NaN) value.

print(df.dropna(axis=1))#drop that columns which contain atleast 1 NaN value
print(df.dropna(axis=0))
#by default axis = 0 i.e row

print(df.dropna(subset=['last_name'])) # remove row in which column last_name is NaN

#fill data

#filling data in place all NaN values
print(df.fillna('0'))

#filling a value of our choice in column/row
print(df['pre_movie_score'].fillna(0))

#filling a value of mean of that that column in place of NaN
print(df['pre_movie_score'].fillna(df['pre_movie_score'].mean()))


airline_tix = {'first':100,'buisness':np.nan,'economy-plus':50,'economy':30}
#here buisness has NaN
#so to fill it with interpolation value between economy-plus and first

ser = Series(airline_tix)
print(ser)
print(ser.interpolate()) #now the NaN value is fill with interplatation value between first and economy-plus






