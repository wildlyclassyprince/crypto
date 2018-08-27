# -*- coding: utf-8 -*-

'''
This script contains the tests for `coinmarketcap_top_5.py`.
'''

__author__="wildlyclassyprince"
__license__="GNU"
__version__="0.1.0"
__maintainer__="wildlyclassyprince"
__email__="lihtumb@gmail.com"
__status__="Initial Tests"

# The usual suspects ...
from datetime import datetime
import pandas as pd
import numpy as np

URL = 'https://coinmarketcap.com/tokens/views/all'

# Using Pandas to return the first table on the page
df = pd.read_html(URL, attrs={'id': 'assets-all'})[0].head()

# New column names:
df.columns = ['#', 'Name', 'Platform', 'MarketCap', 'Price', 'CirculatingSupply',
              'VolumeDay', 'pctHour', 'pctDay', 'pctWeek', 'NewCol']

df = df.drop('NewCol', axis=1)

# Size of data
def test_size_of_dataframe():
    '''Tests the size of the dataframe.'''
    assert(df.shape[1]==10)

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
def coerce_df_columns_to_numeric(df, column_list):
    '''Convert numeric columns to numeric type.'''
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')

coerce_df_columns_to_numeric(df, ['MarketCap', 'Price', 'CirculatingSupply',
                                  'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])

# Value types
def test_numeric_types():
    '''tests if numeric values are of numeric type.'''
    assert isinstance(df['#'][0], np.int64)
    assert isinstance(df['MarketCap'][0], np.int64)
    assert isinstance(df['Price'][0], np.int64)
    assert isinstance(df['CirculatingSupply'][0], np.int64)
    assert isinstance(df['VolumeDay'][0], np.int64)
    assert isinstance(df['pctHour'][0], np.int64)
    assert isinstance(df['pctDay'][0], np.int64)
    assert isinstance(df['pctWeek'][0], np.int64)
    
def test_non_numeric_types():
    '''tests if non-numeric values are of non-numeric type.'''
    assert isinstance(df['Name'][0], np.str)
    assert isinstance(df['Platform'][0], np.str)

if __name__ == '__main__':
    test_size_of_dataframe()
    test_numeric_types()
    test_non_numeric_types()