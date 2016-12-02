#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:06:34 2016

@author: visethsen
"""

import pandas

cc1 = pandas.read_csv('cc1.csv')
gs1 = pandas.read_csv('gs1.csv')
cc2 = pandas.read_csv('cc2.csv')
gs2 = pandas.read_csv('gs2.csv')
cc3 = pandas.read_csv('cc3.csv')
gs3 = pandas.read_csv('gs3.csv')

print("Cleveland Teamstats")
print(cc1.iloc[-1,:])
print("Cleveland Assists")
print(cc1.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc2.iloc[-1,:])
print("Cleveland Assists")
print(cc2.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc3.iloc[-1,:])
print("Cleveland Assists")
print(cc3.iloc[-1,-7])


print(gs1)
print("Golden State Teamstats")
print(gs1.iloc[-1,:])
print ('Golden State Assist')
print (gs1.iloc[-1,-7])

print("Golden State Teamstats")
print(gs2.iloc[-1,:])
print ('Golden State Assist')
print (gs2.iloc[-1,-7])

print("Golden State Teamstats")
print(gs3.iloc[-1,:])
print ('Golden State Assist')
print (gs3.iloc[-1,-7])

assists = int(gs3.iloc[-1,-7]) + int(gs2.iloc[-1,-7]) + int(gs1.iloc[-1,-7])

print ("assists " + str(assists))