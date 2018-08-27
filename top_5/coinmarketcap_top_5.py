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
def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')
    
coerce_df_columns_to_numeric(df, ['MarketCap', 'Price', 'CirculatingSupply',
                                  'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])

# Dataframe sorting functions
def sort_dataframe(df, col, ascending=True):
    '''Returns sorted dataframe values.'''
    return df.sort_values([col], ascending=ascending)

def sort_name(df):
    '''Returns sorted dataframe value names.'''
    return sort_dataframe(df, 'Name', True).iloc[:, [1, 3, 5, 6]].head()

def sort_marketcap(df):
    '''Returns sorted MarketCap values.'''
    return sort_dataframe(df, 'MarketCap', False).iloc[:, [1, 3]].head()

def sort_price(df):
    '''Returns sorted price values.'''
    return sort_dataframe(df, 'Price', False).iloc[:, [1, 4]].head()

def sort_volume(df):
    '''Returns sorted volume values.'''
    return sort_dataframe(df, 'VolumeDay', False).iloc[:, [1, 6]].head()

def sort_hour(df):
    '''Returns sorted hourly percentages.'''
    return sort_dataframe(df, 'pctHour', False).iloc[:, [1, 7]].head()

def sort_day(df):
    '''Returns sorted daily percentages.'''
    return sort_dataframe(df, 'pctDay', False).iloc[:, [1, 8]].head()

def sort_week(df):
    '''Returns sorted weekly percentages.'''
    return sort_dataframe(df, 'pctWeek', False).iloc[:, [1, 9]].head()

# Printing sorted dataframe in a tabulated format:
def print_tabulated(df):
    '''Prints the sorted dataframe in a tabular format.'''
    print(tabulate.tabulate(df, headers='keys', showindex='false', numalign='right'))
    
# Putting it all together:
def report():
    print('Title     : ' + 'CryptoAsset Market Capitalizations (Top 10)')
    print('          : ' + 'Ethereum with Market Cap')
    print('Source    : ' + url)
    print('Time      : ' + str(datetime.now().strftime('%Y-%m-%d %H:%M')))
    print('')
    print('')
    print_tabulated(sort_name(df))
    print('')
    print_tabulated(sort_marketcap(df))
    print('')
    print_tabulated(sort_price(df))
    print('')
    print_tabulated(sort_volume(df))
    print('')
    print_tabulated(sort_hour(df))
    print('')
    print_tabulated(sort_day(df))
    print('')
    print_tabulated(sort_week(df))
    
if __name__ == '__main__':
    report()