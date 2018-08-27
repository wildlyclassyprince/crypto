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
import tabulate
import coinmarketcap_top_5 as top5

URL = 'https://coinmarketcap.com/tokens/views/all'

# Value types
def check_numeric_types():
    '''Checks if numeric values are of numeric type.'''
    assert isinstance(df['MarketCap'], int)
    assert isinstance(df['Price'], int)
    assert isinstance(df['CirculatingSupply', int])
    assert isinstance(df['VolumeDay'], int)
    assert isinstance(df['pctHour'], int)
    assert isinstance(df['pctDay'], int)
    assert isinstance(df['pctWeek'], int)
    
def check_non_numeric_types():
    '''Checks if non-numeric values are of non-numeric type.'''
    assert isinstance(df['#'], str)
    assert isinstance(df['Name'], str)
    assert isinstance(df['Platform'], str)