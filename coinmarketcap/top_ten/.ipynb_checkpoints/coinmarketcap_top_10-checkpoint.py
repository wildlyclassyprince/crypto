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

# Dropping the new column: