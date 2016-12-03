
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

