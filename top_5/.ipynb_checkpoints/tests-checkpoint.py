# -*- coding: utf-8 -*-

'''
This script contains the tests for `coinmarketcap_top_5.py`.
'''

__author__ = "wildlyclassyprince"
__license__ = "GNU"
__version__ = "0.1.0"
__maintainer__ = "wildlyclassyprince"
__email__ = "lihtumb@gmail.com"
__status__ = "Initial Tests"

# The usual suspects ...
import pandas as pd

URL = 'https://coinmarketcap.com/tokens/views/all'

# Using Pandas to return the first table on the page
df = pd.read_html(URL, attrs={'id': 'assets-all'}, encoding='utf-8')[0].head()

# New column names:
df.columns = ['#', 'Name', 'Platform', 'MarketCap', 'Price', 'CirculatingSupply',
              'VolumeDay', 'pctHour', 'pctDay', 'pctWeek', 'NewCol']

df = df.drop('NewCol', axis=1)

# Cleaning numeric data:
df['Name'] = df['Name'].apply(lambda x: x.upper())
df['Price'] = df['Price'].str.replace('$', '')
df['MarketCap'] = df['MarketCap'].str.replace('$', '')
df['MarketCap'] = df['MarketCap'].str.replace(',', '')
df['VolumeDay'] = df['VolumeDay'].str.replace('$', '')
df['VolumeDay'] = df['VolumeDay'].str.replace(',', '')
df['VolumeDay'] = df['VolumeDay'].str.replace('Low Vol', '0')
df['pctHour'] = df['pctHour'].str.replace('%', '')
df['pctDay'] = df['pctDay'].str.replace('%', '')
df['pctWeek'] = df['pctWeek'].str.replace('%', '')

# Filter for rows only containing Ethereum and a MarketCap value
df = df.loc[(df['Platform'] == 'Ethereum') & (df['MarketCap'] != '?')]

# Convert numeric columns to numeric type
def coerce_df_columns_to_numeric(data, column_list):
    '''Convert numeric columns to numeric type.'''
    data[column_list] = data[column_list].apply(pd.to_numeric, errors='coerce')

coerce_df_columns_to_numeric(data=df, column_list=['MarketCap', 'Price', 'CirculatingSupply',
                                                   'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])

# Size of data
def test_size_of_dataframe():
    '''Tests the size of the dataframe.'''
    assert df.shape[1] == 10

# Value types
def test_numeric_types():
    '''Tests numeric values if they are of numeric type.'''
    return None

def test_non_numeric_types():
    '''Tests non-numeric values if they are of non-numeric type.'''
    return None
