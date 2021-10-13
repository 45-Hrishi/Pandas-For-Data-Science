import pandas as pd

'''Often the data you need exists in two separate sources,fortunately,Pandas makes it easy to combine these together.

The simplest combination if both sources are already in the same format,then a concatenation through the "pd.concat()" call is all that is needed

concatenation is simply 'pasting' the two DataFrames together by columns
'''

data_1 = {'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']}
data_2 = {'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']}
index_ = {'1','2','3','4'}
one = pd.DataFrame(data=data_1,index=index_)
two = pd.DataFrame(data=data_2,index=index_)
merge_ = pd.concat([one,two],axis=1)
print(merge_)
'''
we get,
3  A0  B0  C0  D0
2  A1  B1  C1  D1
4  A2  B2  C2  D2
1  A3  B3  C3  D3
'''
#if you want to concat along row then use axis=0, but these throws lot of NaN values so change column name of any DF with any of the DF

one.columns = two.columns
print(one)
new_merge = pd.concat([one,two],axis=0)
# print(new_merge)
'''
we get
   C   D
2  A0  B0
1  A1  B1
3  A2  B2
4  A3  B3
2  C0  D0
1  C1  D1
3  C2  D2
4  C3  D3
'''

#if you want change index ordering then use
new_merge.index = range(len(new_merge))
print(new_merge)

'''
we get new indx order i.e from 0-7,
 C   D
0  A0  B0
1  A1  B1
2  A2  B2
3  A3  B3
4  C0  D0
5  C1  D1
6  C2  D2
7  C3  D3
'''

