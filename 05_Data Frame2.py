import pandas as pd
# **********Columns***********
df = pd.read_csv('tips.csv')
print(df.columns) #prints --> list of all columns name

#************index************
print(df.index) # prints --> start-index end-index and step in between them

#*************head************
print(df.head()) 
'''Enter no of head rows you want to see(by default it shows first 5 rows)'''

#************tail**************
print(df.tail())
''' Enter no of tail rows you want to see(by default it shows last 5 rows)'''

#*************info*************
#shows all information regarding data frame also shows RAM you used for this work
print(df.info()) # memory usage: 21.1+ KB

#***************describe*************
''' NOTE - perform operation only on integer datatype '''
#This function performs many operation on dataframe column like
#count - no of rows
#mean - mean of column
#std - standard deviation
#min - minimum of that column
#max - maximum of that column
#25% 50% 75%
print(df.describe())

''' 
we can also change rows into column by simply calling transpose() method.
'''

