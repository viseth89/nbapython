#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:14:47 2016

@author: visethsen
"""

1
2
import pandas
data_df = pandas.read_csv('gs3.csv')

starters = data_df.iloc[0:5,:]

print(data_df['MP'])
print(data_df.shape)


print('starters')
print(starters)