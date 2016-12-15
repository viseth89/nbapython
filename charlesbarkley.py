<<<<<<< HEAD
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
=======

#Importing of the necessary Modules to make Charts
from matplotlib import pyplot as plt
from matplotlib import style

#Importing Module to read CSV File
import csv

#Simplest way to read a csv file
#Will look to understand the more complicated ways/udacity
#Here we opened our initial csv file

file_names = ['charlesbarkleye.csv','larrybird.csv']

for file in file_names:
    with open (file) as csvfile:
        #Command to read it with arguements***** Still not fully understood
        readCSV = csv.reader(csvfile, delimiter=',')
        #Empty Variables to store the data we want to present
        yr = []
        pts = []
        ast = []
        trb = []
        stl = []
        
        #Pulling the Data from the CSV File a bit of trial and error to find the right columns, aprox 30,
        for row in readCSV:
            year = row[0]
            points = row[29]
            assist = row[24]
            totalrb = row[23]
            steal = row[25]
        #Adding/appending the info from the csv into the varibles that we created above starting at line 23
            yr.append(year)
            pts.append(points)
            ast.append(assist)
            trb.append(totalrb)
            stl.append(steal)
        
        #Styles, want to understand more*****
    style.use('ggplot')
    
    
    
    # Posting of the data in a chart format
    
    #Labeling of the Lines
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

>>>>>>> work
