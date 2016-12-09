#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:03:32 2016

@author: visethsen
"""

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

# variable used to represent games
games = [1,2,3,4,5,6,7]

#Creating Varibles to hold the Read CSV Files
cc1 = pd.read_csv('cc1.csv')
gs1 = pd.read_csv('gs1.csv')
cc2 = pd.read_csv('cc2.csv')
gs2 = pd.read_csv('gs2.csv')
cc3 = pd.read_csv('cc3.csv')
gs3 = pd.read_csv('gs3.csv')
cc4 = pd.read_csv('cc4.csv')
gs4 = pd.read_csv('gs4.csv')
cc5 = pd.read_csv('cc5.csv')
gs5 = pd.read_csv('gs5.csv')
cc6 = pd.read_csv('cc6.csv')
gs6 = pd.read_csv('gs6.csv')
cc7 = pd.read_csv('cc7.csv')
gs7 = pd.read_csv('gs7.csv')


cavs = [cc1,cc2,cc3,cc4,cc5,cc6,cc7]
cpts = []
crbs = []
cast = []
cstl = []
corbs = []

wars = [gs2,gs2,gs3,gs4,gs5,gs6,gs7]
wpts = []
wrbs = []
wast = []
wstl = []
worbs = []

for game in cavs:
    cast.append(game.iloc[-1,-7])
    cstl.append(game.iloc[-1,-6])
    crbs.append(game.iloc[-1,-8])
    corbs.append(game.iloc[-1,-10])
    cpts.append(game.iloc[-1,-2])
    
print (cast)
print (cstl)
print('rebounds')
print (crbs)
# Want to find a how to call using .ix[-1,'AST']


for game in wars:
    wast.append(game.iloc[-1,-7])
    wstl.append(game.iloc[-1,-6])
    wrbs.append(game.iloc[-1,-8])
    worbs.append(game.iloc[-1,-10])
    wpts.append(game.iloc[-1,-2])
    
plt.plot(games,cpts,'g')
plt.plot(games,cast,'c')
plt.plot(games,crbs,'r')
plt.plot(games,corbs,'m')
plt.plot(games,cstl,'b')

plt.show()

plt.plot(games,wpts,'g',label ='Pts')
plt.plot(games,wast,'c',label='Assist')
plt.plot(games,wrbs,'r', label = 'Rebounds')
plt.plot(games,worbs,'m', label = 'O Rebound')
plt.plot(games,wstl,'b', label = 'Steals')


plt.xlabel('Game')
plt.legend()
plt.show()

    
'''
plt.plot(yr,pts,'g',label='points', linewidth=5)
plt.plot(yr,ast,'c',label='assists',linewidth=5)
plt.plot(yr,trb,'r',label='rebounds',linewidth=5)
plt.plot(yr,stl,'m',label='steals',linewidth=5)

#Labeling the Outside of the chart
plt.title('Charles Barkley\nRound Mound of Rebound')
plt.ylabel('Statistics')
plt.xlabel('Year')

#Showing the Legend for the chart
plt.legend()

plt.grid(True,color='k')
#Showing Chart?
plt.show()
'''

'''
>>> df.recency
>>> df['recency']
>>> df[['recency']]
>>> df.loc[:, 'recency']
>>> df.loc[:, ['recency']]
>>> df.iloc[:, 0]
>>> df.iloc[:, [0]]
>>> df.ix[:, 0]
'''