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





'''
plt.bar([1,3,5,7,9], [5,2,7,8,2], label='example numero 1')
plt.bar([2,4,6,8,10], [4,6,8,4,10], label='part 2', color='g')
plt.legend
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('bar graph title\nAnother Line Whoa')

plt.show()
# Plotting x and y which would be the data
'''
