# -*- coding: utf-8 -*-

'''
This script makes the coinmarketcap_top_5.py file accessible  from
the command line.
We will use entry points as a modular plug-in architecture.
'''

# The suspect ...
from setuptools import setup

# The setup
setup(
    name='top5',
    entry_points={
        'console_scripts':[
            'top5=coinmarketcap_top_5:report',
        ],
    },
    author="wildlyclassyprince",
    email="lihtumb@gmail.com",
    license="GNU",
    version="0.1.0",
    url="https://github.com/wildlyclassyprince/crypto/tree/master/top_5"
)
