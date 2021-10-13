import pandas as pd
import numpy as np
df = pd.read_csv('tips.csv')
'''
#if we want to apply any operation on any column then make one function and using 'apply'method apply that on favourable column

def last_four(num):
    return str(num)[-4:]

print(df['CC Number'].apply(last_four)) #using this method wew get column of last four numbers of CC Number

df['last_four'] = df['CC Number'].apply(last_four) #creation of new column
print(df['last_four'])
print(df)'''

def yelp(price):
    if price < 10:
        return '$'
    elif price >=10 and price < 30:
        return '$$'
    else:
        return '$$$'

df['yelp'] = df['total_bill'].apply(yelp)
print(df)







