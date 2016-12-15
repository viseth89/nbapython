import csv

with open ('charlesbarkley.csv') as csvfile:
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
        
        print(row[0],row[29], row[24], row[23],row[25])
        
  

    print (x)
        