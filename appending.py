import csv

with open ('charlesbarkleye.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    yr = []
    pts = []
    ast = []
    trb = []
    stl = []
    
    
    for row in readCSV:
        year = row[0]
        points = row[29]
        assist = row[24]
        totalrb = row[23]
        steal = [25]

        yr.append(year)
        pts.append(points)
        ast.append(assist)
        trb.append(totalrb)
        stl.append(steal)
        
    print (yr)
       
    yr = yr[[0:4]]

    print (yr)    
  

  
        