# Top 5

This script downloads data from `CryptoCurrency Market Capitalizations` and filters for the top 5 data with a Market Cap. Data is downloaded from [CoinMarketCap](https://coinmarketcap.com/).

Requirements:
>- pandas (0.23.0)
>- tabulate (0.82)
>- datetime (4.2)
>- setuptools (39.1.0)

Data is downloaded from [`https://coinmarketcap.com/tokens/views/all`](https://coinmarketcap.com/tokens/views/all)

When we download the data, not all values are in the appropriate formats. Most are coerced to be string objects. To convert numeric columns to numeric values, we have the function:
```python
def coerce_df_columns_to_numeric(df, column_list):
    df[column_list] = df[column_list].apply(pd.to_numeric, errors='coerce')
```

And we use it to convert _Market Cap, Price, Circulating Supply, Volume (24h), Hourly, Daily and Weekly Percentages_ to numeric values:
```python
coerce_df_columns_to_numeric(df, ['MarketCap', 'Price', 'CirculatingSupply',
                                  'VolumeDay', 'pctHour', 'pctDay', 'pctWeek'])
```

We also need to sort the order of values before we print out the output. We define a function that returns sorted values of the dataframe based the column we wish to sort:
```python
def sort_dataframe(df, col, ascending=True):
    '''Returns sorted dataframe values.'''
    return df.sort_values([col], ascending=ascending)
```

The output is printed in a _pretty_ tabulatar format using the function:
```python
def print_tabulated(df):
    '''Prints the sorted dataframe in a tabular format.'''
    print(tabulate.tabulate(df, headers='keys', showindex='false', numalign='right'))
```

All the output is wrapped to together by the `report()` function, which prints all the output.

The `coinmarketcap_top_5.py` file has a `setup.py` file which enables us to access the `coinmarketcap_top_5.py` file from the commandline ... :notes:

To build:
```shell
$ python3 setup.py develop
```

To run the program:
```shell
$ top5
```

### To-Do

- [x] Add `setup.py` for running script in terminal.
- [ ] Write tests for the script.
- [ ] Carry out initial tests.
- [ ] Add support for other cryptos (Current implementation is for Ethereum only).