
"""
Created on Sat Nov 19 22:43:46 2016

@author: visethsen
Working ON Golden State Team Data
"""

#Importing of the necessary Modules to make Charts
from matplotlib import pyplot as plt
from matplotlib import style

#Importing Module to read CSV File
import csv

#Simplest way to read a csv file
#Will look to understand the more complicated ways/udacity
#Here we opened our initial csv file
with open ('gs2016e.csv') as csvfile:
    #Command to read it with arguements***** Still not fully understood
    readCSV = csv.reader(csvfile, delimiter=',')
    #Empty Variables to store the data we want to present
    yr = []
    #This is For GS's Team
    pts = []
    orb = []
    trb = []
    ast = []
    stl = []
    blk = []
    to = []
    #This is for the Opponents Team
    opts = []
    oorb = []
    otrb = []
    oast = []
    ostl = []
    oblk = []
    oto = []

    
    dpts = []
    #Pulling the Data from the CSV File a bit of trial and error to find the right columns, aprox 30,
    for row in readCSV:
        year = row[0]
    #Creating Variables for Golden States Team
        points = row[3]
        offenserb = row[6]
        totalrb = row[7]
        assist = row[8]
        steal = row[9]
        block = row[10]
        turno = row[10]

    #Creating for Opponents
    
        opoints = row[4]
        ooffenserb = row[12]
        ototalrb = row[13]
        oassist=row[14]
        osteal=row[15]
        oblock=row[16]
        oturno=row[17]
    #Adding/appending the info from the csv into the varibles that we created above starting at line 23
        yr.append(year)
        pts.append(points)
        orb.append(offenserb)
        trb.append(totalrb)
        ast.append(assist)
        stl.append(steal)
        blk.append(block)
        to.append(turno)
        
    #Appending Opponent
        opts.append(opoints)
        oorb.append(ooffenserb)
        otrb.append(ototalrb)
        oast.append(oassist)
        ostl.append(osteal)
        oblk.append(oblock)
        oto.append(oturno)
        
        dpts.append(int(points)-int(opoints))
        #We wrote this but don't quite understand... must research
    
    print (dpts)
    print (max(dpts))
    print ("Biggest win difference")
    print (min(dpts)) 
    print ("loss diff")
    #Testing 
    
    
    
    #Styles, want to understand more*****

style.use('ggplot')



# Posting of the data in a chart format

#Labeling of the Lines
plt.plot(yr,pts,'g',label='points', linewidth=5)
plt.plot(yr,ast,'c',label='assists',linewidth=5)
plt.plot(yr,trb,'r',label='rebounds',linewidth=5)
plt.plot(yr,stl,'m',label='steals',linewidth=5)
plt.plot(yr,dpts,'g',label='point difference', linewidth=10)

#Labeling the Outside of the chart
plt.title('Golden State Warriors')
plt.ylabel('Statistics')
plt.xlabel('Game')

#Showing the Legend for the chart
plt.legend()

plt.grid(True,color='k')
#Showing Chart?
plt.show()

