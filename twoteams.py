#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:36:34 2016

@author: visethsen
"""
'''
Analysis of Two Teams
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 20:36:34 2016

@author: visethsen
"""
'''
Analysis of Two Teams
'''
# 1 We Begin by importing the modules we need
import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd


# Creation of the Class Team to store all our data
class Team:
    def __init__(self, t):
        self.wins = t[t["W/L"]=='W']
        self.loss = t[t['W/L']=='L']
        self.assist_w=t[t['AST']>t['AST.1']]
        self.assist_l=t[t['AST']<t['AST.1']]
        self.trebounds_w=t[t['TRB']>t['TRB.1']]
        self.trebounds_l=t[t['TRB']<t['TRB.1']]
        self.orb_w=t[t['ORB']>t['ORB.1']]
        self.orb_l=t[t['ORB']<t['ORB.1']]
        self.to_w=t[t['TOV']>t['TOV.1']]
        self.to_l=t[t['TOV']<t['TOV.1']]
        self.stl_w=t[t['STL']>t['STL.1']]
        self.stl_l=t[t['STL']<t['STL.1']]
        self.blk_w=t[t['BLK']>t['BLK.1']]
        self.blk_l=t[t['BLK']<t['BLK.1']]
        self.wrebounds_w=self.trebounds_w[self.trebounds_w["W/L"] =="W"]
        self.wassist_w=self.assist_w[self.assist_w['W/L']=='W']

        self.astreb = self.assist_w[self.assist_w['TRB'] > self.assist_w['TRB.1']]

        self.astrebw = self.astreb[self.astreb['W/L']=='W']
        
        self.wpct = (len(self.wrebounds_w)) / (len(self.trebounds_w))
        self.wwpct = (len(self.wassist_w)) / (len(self.assist_w))
        self.wwwpct = len(self.astrebw)/len(self.astreb)
                

df1 = pd.DataFrame.from_csv('data/team1.csv')
df2 = pd.DataFrame.from_csv('data/team2.csv')        
teams = [df1,df2]
read_teams=[]


for df in teams:
    team = Team(df)
    read_teams.append(team)
    

team1 = read_teams[0]
team2 = read_teams[1]

team1.wins
#Using this as a test to replicate and understand better what you showed me


