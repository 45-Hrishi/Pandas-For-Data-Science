from numpy.lib.shape_base import split
import pandas as pd
import numpy as np
from datetime import datetime as dt
from pandas.core.algorithms import value_counts
from pandas.core.indexes.base import Index
hotels = pd.read_csv('hotel_booking_data.csv')

'''
print(hotels.head())
#How many Rows are there?
print(len(hotels))
'''

#Which column has most missing data?
print(hotels.isnull().sum())

#Drop the company column from dataset
print(hotels.drop('company',axis=1))

#What are the top 5 most common country codes in the dataset?
print(hotels['country'].value_counts()[:5])
#another approach
print(hotels.groupby('country').count().sort_values('hotel',ascending=False)[:5]['hotel'])


#What is the name of the person who paid the highest ADR? How much was their ADR?
print(hotels.sort_values('adr',ascending=False)[['adr','name']].iloc[0])
#getting exact position of highest adr
print(hotels['adr'].idxmax())
#returns the maximum index of column value
'''
adr            5400.0
name    Daniel Walter
Name: 48515, dtype: object
'''

#What is the mean adr across all the hotel stays in the dataset?
print(round(hotels['adr'].mean(),2))


#What is the average number of nights for a stay across the entire data set? Feel free to round this to 2 decimal point
print(round((hotels['stays_in_weekend_nights']+hotels['stays_in_week_nights']).mean(),2))


#What is the average total cost for a stay in the dataset?Not average daily cost,but total stay cost(You will need to calculate total cost your self by using ADR and week day and weeknight stays).Feel free to round this to 2 decimal points
total_days = (hotels['stays_in_weekend_nights']+hotels['stays_in_week_nights'])
total_cost = total_days*hotels['adr']
print(round(total_cost.mean(),2))


#What are the names and emails of the people who made exactly 5 'Special Request'?
print(hotels[hotels['total_of_special_requests'] == 5][['name','email']])

#What percentage of hotel stays were classified as "repeat guests"?(Do not base this off the name of the person, but instead of the is_repeated_guest_column)
total_repeat_guests = hotels[hotels['is_repeated_guest']>0][['is_repeated_guest']].sum()
percent_repeated = total_repeat_guests/len(total_days)*100
print(round(percent_repeated,2))


#What are the top 5 most common last names in dataset?
def last_name(name):
    last_nme = str(name).lower().split()[1]
    return last_nme.capitalize()

Last_names = hotels['name'].apply(last_name)
print(Last_names.value_counts()[:5])

#What are the number of peoples who had booked the most number childrens and babies for their stay?
hotels['total_kids'] = hotels['babies'] + hotels['children']

print(hotels.sort_values('total_kids',ascending=False)[['name','adults','total_kids','babies','children']][:3])

#What are the top 3 most common phone codes?
def area_code(number):
    return str(number).split('-')[0]
most_common_area_code = hotels['phone-number'].apply(area_code).value_counts(ascending=False)[:3]
print(most_common_area_code)


#How many arrivals took place in between 1st and the 15th of every month (inclusive 1 and 15)?
total = hotels['arrival_date_day_of_month'].between(1,15).sum()
print(total)


#Create a table for counts for each day of the week that people arrived 
def convert(day,month,year):
    return f'{day}-{month}-{year}'

hotels['date'] = np.vectorize(convert)(hotels['arrival_date_day_of_month'],hotels['arrival_date_month'],hotels['arrival_date_year'])

#print(hotels['date'])#29-August-2017
hotels['date'] = pd.to_datetime(hotels['date'])
#print(hotels['date'])#2017-08-29
#print(hotels['date'].dt.day_name())#Tuesday
print(hotels['date'].dt.day_name().value_counts())

