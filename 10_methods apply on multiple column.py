import pandas as pd
import numpy as np
import timeit

df =  pd.read_csv('tips.csv')
#df['total_bill'].apply(lambda num:num*2) --> use of lambda function 

def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return 'Generous'
    else:
        return 'Other'

print(df[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']),axis=1))

#Vectorization is used to speed up the Python code without using loop. Using such a function can help in minimizing the running time of code efficiently.
df['Quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])

#above both method prints the same output
print(df['Quality'])


#now to remove confusion let's take timeit module and calculate which method is run faster
setup = '''
import pandas as pd
import numpy as np

df =  pd.read_csv('tips.csv')
def quality(total_bill,tip):
    if tip/total_bill > 0.25:
        return 'Generous'
    else:
        return 'Other'
'''

stmt_one = '''
df['Quality'] = df[['total_bill','tip']].apply(lambda df:quality(df['total_bill'],df['tip']),axis=1)
'''

stmt_two = '''
df['Quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])
'''

time_one = timeit.timeit(setup=setup,stmt=stmt_one,number=1000)
print(time_one)# 5.0720224 seconds

time_two = timeit.timeit(setup=setup,stmt=stmt_two,number=1000)
print(time_two)# 0.3973152000000004 seconds 

# from above results it's clear that vectorize method is much faster than lambda one
