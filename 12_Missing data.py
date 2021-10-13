'''
1. Real world data will often be misssing data for a variety of reasons.

2. Many machine learning models and statistical methods can not work with missing data points ,in which case we need to decide what to do with the missing data.

3. When reading in missing values.pandas will display them as NaN valueds.

4. There are also newer specialized null values such as pd.NaT to imply the value missing should be a timestamp.

options for missing data
keep it
remove it
replace it

note that there is never a 100% correct approach that applies to all circumstances, it all depends on the exact situation you encounter.

Removing or Dropping missing data
Dropping a Row --> makes a sense when a lot of info is missing

            Year        Pop         GDP         Area
USA         1776        NaN         NaN         NaN
CANADA      1867        38          1.7         3.86
MEXICO      1821        126         1.22        0.76

---> Dropping USA row is the right decision becoz we have missing lot of data of that row
---> Often a good idea to calculate a percentage of what data is droppe
---> Good choice if every row is missing that particular feature.
'''

