from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
from pandas.io.stata import StataStrLWriter

df = pd.read_csv('Sales_Funnel_CRM.csv')
print(df)
# print(help(pd.pivot))

licenses = df[['Company','Product','Licenses']]
# print(licenses)
pivt = pd.pivot(data=licenses,index='Company',columns='Product',values='Licenses')
print(pivt)

pivot_tb = pd.pivot_table(df,index='Company',aggfunc=[np.sum],values=['Licenses','Sale Price'])
# pivot_tb = pivot_tb[pivot_tb['Sale Price'] > 3500000]
print(pivot_tb)

table = pd.pivot_table(df,index=['Account Manager','Contact'],values=['Sale Price'],columns=['Product'],aggfunc='sum',fill_value='0',margins = True)#margins = True --> Grand total at last
print(table)


# html_table = table.to_html('sample_html_pivot.html',index=False)
# print(html_table)