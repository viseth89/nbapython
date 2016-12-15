
"""
Created on Sat Nov 19 22:43:46 2016

@author: visethsen
"""

#Importing of the necessary Modules to make Charts
from matplotlib import pyplot as plt
from matplotlib import style

#Importing Module to read CSV File
import csv

#Simplest way to read a csv file
#Will look to understand the more complicated ways/udacity
#Here we opened our initial csv file
with open ('1997bullsgamelong.csv') as csvfile:
    #Command to read it with arguements***** Still not fully understood
    readCSV = csv.reader(csvfile, delimiter=',')
    #Empty Variables to store the data we want to present
    
    gm = []
    orb = []
    trb = []
    ast = []
    stl = []
    blk = []
    
    ogm = []
    oorb = []
    otrb = []
    oast = []
    ostl = []
    oblk = []
    #Pulling the Data from the CSV File a bit of trial and error to find the right columns, aprox 30,
    for row in readCSV:
        
        game = row[1]

        offenserb = row[17]
        totalrb = row[18]
        assist = row[19]
        steal = row[20]
        block = row[21]
    #Adding/appending the info from the csv into the varibles that we created above starting at line 23
        gm.append(game)
        orb.append(offenserb)
        trb.append(totalrb)
        ast.append(assist)
        stl.append(steal)
        blk.append(block)
 
    #Opponent Data set and appends
    
        ooffenserb = row[34]
        ototalrb = row[35]
        oassist = row[36]
        osteal = row[37]
        oblock = row[38]
    #Appends
        ogm.append(game)
        oorb.append(ooffenserb)
        otrb.append(ototalrb)
        oast.append(oassist)
        ostl.append(osteal)
        oblk.append(oblock)
        
        
        
        
        print (row[1],row[4:8],row[17:22],row[34:39])
    
    #Styles, want to understand more*****
style.use('ggplot')



# Posting of the data in a chart format

#Labeling of the Lines
plt.plot(gm,orb,'g',label='orebounds', linewidth=5)
plt.plot(gm,ast,'c',label='assists',linewidth=5)
plt.plot(gm,trb,'r',label='rebounds',linewidth=5)
plt.plot(gm,stl,'m',label='steals',linewidth=5)
plt.plot(gm,blk,'y',label='block',linewidth=5)


#Labeling the Outside of the chart
plt.title('Bulls 1997')
plt.ylabel('Statistics')
plt.xlabel('Game')

#Showing the Legend for the chart
plt.legend()

plt.grid(True,color='k')
#Showing Chart?
plt.show()


#Labeling of the Lines of the opponent
plt.plot(gm,oorb,'g',label='orebounds', linewidth=5)
plt.plot(gm,oast,'c',label='assists',linewidth=5)
plt.plot(gm,otrb,'r',label='rebounds',linewidth=5)
plt.plot(gm,ostl,'m',label='steals',linewidth=5)
plt.plot(gm,oblk,'y',label='block',linewidth=5)


plt.title('Opponent 1997')
plt.ylabel('Statistics')
plt.xlabel('Game')

plt.show()
'''
plt.hist(oorb, oast, otrb, ostl, oblk, histtype='bar', rwidth=0.8)

plt.show()
'''

import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(oorb, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
