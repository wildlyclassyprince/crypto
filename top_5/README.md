# Top 5

This script downloads data from `CryptoCurrency Market Capitalizations` and filters for the top 5 data with a Market Cap. Data is downloaded from [CoinMarketCap](https://coinmarketcap.com/).

Requirements:
>- pandas (0.23.0 or higher)
>- tabulate (0.82)
>- datetime (4.2)

Data is downloaded from [`https://coinmarketcap.com/tokens/views/all`](https://coinmarketcap.com/tokens/views/all)

To convert numeric columns to numeric values, we have the function:
```python
def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')
```

Where we convert _Market Cap, Price, Circulating Supply, Volume (24h), Hourly, Daily and Weekly Percentages_ to numeric values:
```python
coerce_df_columns_to_numeric(df, ['MarketCap', 'Price', 'CirculatingSupply',
                                  'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])
```

We need to sort the order of values before we print out the output. We define a function that returns sorted values of the dataframe based the column we wish to sort by:
```python
def sort_dataframe(df, col, ascending=True):
    '''Returns sorted dataframe values.'''
```