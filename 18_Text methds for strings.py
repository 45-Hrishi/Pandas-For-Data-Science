from os import replace
import pandas as pd
'''
NOTE: we use apply() for aplpying function
'''
#*************split()***************
gmail = 'hrishikeshkothawade1@gmail.com'
print(gmail.split('@'))

names = pd.Series(['andrew','bobo','clarie','david','5'])
print(names)
'''
0    andrew
1      bobo
2    clarie
3     david
4         5 '''
print(names.str.upper())#this result is not permanent but to make it permanent use reassignment 
print(names.str.isdigit())#get boolean value true or false whether element is int or not.
'''
0    False
1    False
2    False
3    False
4     True
'''

tech_finance = ['goog,amzn,fb','tcs,ifs,temhdr']
# print(len(tech_finance)) 2
#make Series of list
tickers = pd.Series(tech_finance)
lst = 'goog,amzn,fb'
# print(lst.split(',')[0]) 'goog'


#*****************Filtering messay names*******************
messy_names = pd.Series(['andrew   ','bo;bo','  hrishi'])
# print(messy_names)
'''
0    andrew
1        bo;bo
2       hrishi
'''

#replace ';' with '' 
messy_names = messy_names.str.replace(';','')
'''
we get,
0    andrew
1         bobo
2       hrishi
'''
print(messy_names.str.strip())
'''
we get,
0    andrew
1      bobo
2    hrishi
'''

'''
NOTE : we also make function and specifies all logic their and apply this using .apply()
'''
def cleanup(name):
    name = name.replace(';','')
    name = name.strip()
    name = name.capitalize()
    return name

print(messy_names.apply(cleanup))
'''
we get,
0    Andrew
1      Bobo
2    Hrishi
'''
