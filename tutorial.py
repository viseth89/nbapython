#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:06:19 2016

@author: visethsen
"""

import matplotlib.pyplot as plt
# Importing matplotlib general way that it is used

x1 = [1,2,3]
y1 = [4,7,5]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x1, y1, label = "first line")
plt.plot(x2, y2, label = 'second line')

plt.xlabel('this is the x label')
plt.ylabel('this is the y label')
plt.title('this is how we put the title')
plt.legend()
plt.show()



a1 = [1,2,3]
b1 = [4,7,5]

a2 = [1,2,3]
b2 = [10,14,12]

plt.plot(a1, b1, label = "third line")
plt.plot(a2, b2, label = 'fourth line')

plt.xlabel('this is the x label')
plt.ylabel('this is the y label')
plt.title('this is how we put the title')
plt.legend()
plt.show()






plt.bar([1,3,5,7,9], [5,2,7,8,2], label='example numero 1')
plt.bar([2,4,6,8,10], [4,6,8,4,10], label='part 2', color='g')
plt.legend
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('bar graph title\nAnother Line Whoa')

plt.show()
# Plotting x and y which would be the data

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, color='r')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


win_diff = [2,2,4,4,6,2,2,1,2,4,6]

bins = [1,2,3,4,5,6]

plt.hist(win_diff, bins, histtype='bar', rwidth=1.2)
plt.show()

