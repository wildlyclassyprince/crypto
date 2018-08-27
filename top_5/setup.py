# -*- coding: utf-8 -*-

'''
This script makes the coinmarketcap_top_5.py file accessible  from
the command line.
We will use entry points as a modular plug-in architecture.
'''

__author__ = "wildlyclassyprince"
__license__ = "GNU"
__version__ = "0.1.0"
__maintainer__ = "wildlyclassyprince"
__email__ = "lihtumb@gmail.com"
__status__ = "Initial Script"

# The suspect ...
from setuptools import setup

# The setup
setup(
    name='top5',
    entry_points={
        'console_scripts':[
            'top5=coinmarketcap_top_5:report',
        ],
    }
)
