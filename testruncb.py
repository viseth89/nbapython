  
from matplotlib import pyplot as plt
from matplotlib import style


import csv

with open ('1997bullsgamelong.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    yr = []
    pts = []
    ast = []
    trb = []
    stl = []
    v = 0
    
    
    for row in readCSV:
        year = row[5]
        points = row[29]
        assist = row[24]
        totalrb = row[23]
        steal = row[4]

        yr.append(year)
        pts.append(points)
        ast.append(assist)
        trb.append(totalrb)
        stl.append(steal)
    
    print (row[5])
    print ('test')
    print (yr)
    print (stl)
    print (v) 
    print ('first')
    if yr == 'W':
       v = v + 1
       
       
print (v)
        
style.use('ggplot')

"""
Previous stats

#v = Rebounds
v = [12, 13, 12, 10, 11, 12, 11, 11, 12, 14, 11, 12]
#z = Assissts 
z = [3, 4, 4, 4, 4, 4, 5, 5, 4, 4, 5, 3]
# y = Points
y = [28, 25, 25, 27, 23, 25, 22, 23, 23, 19, 15,16]
#x = Year Played
x = [1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
"""


#manually putting in the stats from http://www.basketball-reference.com/players/p/pippesc01.html



# can plot specifically, after just showing the defaults:
'''
plt.plot(yr,pts,'g',label='points', linewidth=5)
plt.plot(yr,ast,'c',label='assists',linewidth=5)
plt.plot(yr,trb,'r',label='rebounds',linewidth=5)
plt.plot(yr,stl,'m',label='steals',linewidth=5)

plt.title('Charles Barkley')
plt.ylabel('Statistics')
plt.xlabel('Year')

plt.legend()

plt.grid(True,color='k')

plt.show()
'''

# I want to find a more efficient way vs me having to type everything in manually