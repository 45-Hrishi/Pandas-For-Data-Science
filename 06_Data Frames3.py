import pandas as pd
import numpy as np
df = pd.read_csv('tips.csv')
#print(df.columns)
print(df['total_bill']) # we get total_bill column information
mycols = ['total_bill','tip']
print(df[mycols]) # prints --> total_bill and tips columns

# For calculation of tip percentage w.r.t total_bill
print((df['tip'] / df['total_bill'])*100)

#********************adding column*************************
#If you want to give name to the column then use 

# df['tip_percent'] = ((df['tip'] / df['total_bill'])*100)
# print(df)
df['tip_percent'] = np.round(((df['tip'] / df['total_bill'])*100),2)
# print(df)


# *******************removing column************************
print(df.drop('tip_percent',axis=1)) #from here column get drop, column dropped temporary not permenantly
print(df) 
print(df.columns)

#for permenant dropping of column --> store dopping value in df and do next operation on it
df = df.drop('tip_percent',axis=1)
print(df) #---> prints the expected result

# **********************shape()***********************
print(df.shape) #prints --> (244,11) thats why we use axis=1 for columns and axis=0 for row.



