import pandas as pd
q1 = {'Japan':80,'China':450,'India':200,'USA':250}
q2 = {'Brazil':100,'China':500,'India':210,'USA':260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)


print(sales_q1)
print(sales_q2)

#*****************To print out keys of any Series*************************
print(sales_q1.keys()) #prints ---> Index(['Japan', 'China', 'India', 'USA'], dtype='object')


#*****************Perform any arithematic operation directly on Series****************
print(sales_q1/100)
print(sales_q1*2)
print(sales_q1) # but perform operation on Series can't change items present in that Series

print(sales_q1 + sales_q2)
'''
it prints --->

Brazil      NaN
China     950.0
India     410.0
Japan       NaN
USA       510.0

NaN - becoz in q1 there is no brazil and in q1 there is no japan in dictionary
'''
print(sales_q1.divide(sales_q2))
''' It prints --->
Brazil         NaN
China     0.900000
India     0.952381
Japan          NaN
USA       0.961538
'''
print(sales_q1.add(sales_q2))
# to avoid that NaN we use 
# fill_value attribute of add function

print(sales_q1.add(sales_q2,fill_value=0))
#now we will get the desired output i.e Brazil    100.0
'''
Output : 
Brazil    100.0
China     950.0
India     410.0
Japan      80.0
USA       510.0
'''





