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
v = [12, 13, 12, 10, 11, 12, 11, 11, 12, 14, 11, 12]
#z = Assissts 
z = [3, 4, 4, 4, 4, 4, 5, 5, 4, 4, 5, 3]
# y = Points
y = [28, 25, 25, 27, 23, 25, 22, 23, 23, 19, 15,16]
#x = Year Played
x = [1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]

#manually putting in the stats from http://www.basketball-reference.com/players/p/pippesc01.html



# can plot specifically, after just showing the defaults:

plt.plot(x,y,'g',label='points', linewidth=5)
plt.plot(x,z,'c',label='assists',linewidth=5)
plt.plot(x,v,'r',label='rebounds',linewidth=5)

plt.title('Charles Barkley')
plt.ylabel('Statistics')
plt.xlabel('Year')

plt.legend()

plt.grid(True,color='k')

plt.show()

# I want to find a more efficient way vs me having to type everything in manually