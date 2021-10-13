import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

#********************df.describe()******************
print(df.describe()) 

#********************df.transpose()*****************
print(df.transpose())

#********************Sorting method*****************
print(df.sort_values('tip',ascending=True))
#by default ascending is True 

#*****************Sort by multiple columns****************
#if tip value is same for some row then we sort it by size
print(df.sort_values(['tip','size']))

#****************maximum value of any column*******************
print(df['total_bill'].max())#prints --> 50.81

#**************get the index of maximum value******************
print(df['total_bill'].idxmax())#prints index of maximum value --> 170
#Same thing for minimum values.

#checking of correlation between columns
print(df.corr())


#********************Categorical values Sorting***********************
print(df['sex'].value_counts())#prints --> Male:157 Female:87

#******************getting unique values and no of unique values***********************
print(df['day'].unique())#prints --> ['Sun' 'Sat' 'Thur' 'Fri']
print(df['day'].nunique())#prints --> 4

#******************replacing values of any column************************
print(df['sex'].replace('Female','F'))
print(df['sex'].replace('Male','M'))

                    # if replace many values use list like this
print(df['sex'].replace(['Female','Male'],['F','M'])) 


#*******************Map method for repalcing column values********************
mymap = {'Female':'F','Male':'M'}
print(df['sex'].map(mymap))  #same result like previous one

#********************** detect duplicated itemes in the column******************
simple_df = pd.DataFrame([1,2,2,2],['a','b','c','d'])
print(simple_df.duplicated()) #prints ---> a    False
                                          #b    False
                                          #c     True
                                          #d     True

#********************deleting / dropping duplicate items*********************
print(simple_df.drop_duplicates())#prints --> a  1
                                             #b  2


#******************values between some range**************************
print(df[df['total_bill'].between(10,20,inclusive=True)]) #it prints --> total data frame that contains total_bill in between 10 and 20


#***************nlargest values in any column of df*******************
print(df.nlargest(2,'tip')) #it prints --> first two rows that contains largest tip among all tip values


#same for nsmallest

