#*****************working with row*******************
import numpy as np
import pandas as pd

df = pd.read_csv('tips.csv')
df = df.set_index('Payment ID')
'''
print(df.index)
#**********************Set Index*************************
print(df.set_index('Payment ID')) #setting up Payment ID as index of table --> so 1 column decreases

#*********************** reset index to column *********************
df.reset_index() #--> this will reset the index to column again
print(df.head()) 

#*******************getting information of any row **********************
#getting inforamtion of any row using position(integer) as parameter.
print(df.iloc[0]) #--> prints all information related to that location row

'''

#**********************access of multiple rows********************
print(df.iloc[0:4])#--> use of python slicing function

   #accessing non-serial rows using list method
print(df.loc[['Sun2959','Sun5260']])


#************************Remove/Delete Row********************
print(df.drop('Sun2959',axis=0))
print(df) #--> not permanent removal of row

#to remove it permanently used reassignment of dataframe

#************************Inserting Row*************************
one_row = df.iloc[0]
print(one_row)
df = df.append(one_row)
print(df)