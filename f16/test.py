#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:14:47 2016

@author: visethsen
"""

1
2
import pandas
data_df = pandas.read_csv('in_data.csv')

print(data_df.columns)

colHH = data_df['colHH']
Or if the column name is a valid Python variable name:

1
colHH = data_df.colHH