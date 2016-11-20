#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:51:22 2016

@author: visethsen
"""

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
#v = Rebounds
v = [4, 6, 7, 7, 8, 8, 9, 8, 6, 7, 5, 7]
#z = Assissts 
z = [2, 4, 5, 6, 7, 6, 6, 6, 5, 6, 6, 6 ]
# y = Points
y = [8, 15, 16, 18, 21, 19, 22, 21, 19, 20, 19, 14]
#x = Year Played
x = [1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]

#manually putting in the stats from http://www.basketball-reference.com/players/p/pippesc01.html



# can plot specifically, after just showing the defaults:

plt.plot(x,y,'g',label='points', linewidth=5)
plt.plot(x,z,'c',label='assists',linewidth=5)
plt.plot(x,v,'r',label='rebounds',linewidth=5)

plt.title('Scottie Pippen')
plt.ylabel('Statistics')
plt.xlabel('Year')

plt.legend()

plt.grid(True,color='k')

plt.show()

# I want to find a more efficient way vs me having to type everything in manually