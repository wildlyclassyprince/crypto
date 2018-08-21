# -*- coding: utf-8 -*-

'''
This script downloads data from `CryptoCurrency Market Capitalizations`.
It filters for Ethereum data with a Market Cap.
Data is downloaded from https://coinmarketcap.com/tokens/views/all/
'''

__author__ = "wildlyclassyprince"
__license__ = "GNU"
__version__ = "0.1.0"
__maintainer__ = "wildlyclassyprince"
__email__ = "lihtumb@gmail.com"
__status__ = "Initial Script"

# The usual suspects ...
import pandas as pd
import tabulate

# And their accomplices ...
from datetime import datetime

# Data location
url = 'https://coinmarketcap.com/tokens/views/all'

# Using Pandas to return the first table on the page
df = pd.read_html(url, attrs={'id': 'assets-all'})[0]

# New column names (there is a new column at the end of the column list):
df.columns = ['#', 'Name', 'Platform', 'MarketCap', 'Price', 'Supply', 'VolumeDay', 'pctHour', 'pctDay', 'pctWeek', 'NewCol']

# Dropping the new column
df = df.drop('NewCol', axis=1)

# Cleaning numeric data:
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

# Conver numeric columns to numeric type
def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')
    
coerce_df_columns_to_numeric(df, ['MarketCap', 'Price', 'Supply', 'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])

# Dataframe sorting functions
def sort_dataframe(df, col, ascending=True):
    '''Returns sorted dataframe values.'''
    return df.sort_values([col], ascending=ascending)

def sort_name(df):
    '''Returns sorted dataframe value names.'''
    return sort_dataframe(df, 'Name')