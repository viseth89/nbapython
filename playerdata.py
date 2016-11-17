from __future__ import print_function
from nba_py import player

# endpoint currently disabled on stats.nba.com
# pd = player._PlayerDashboard('203507')
# print(pd.starting_position())

ap = player.PlayerList()
print(ap.info())

pc = player.PlayerSummary('203506')
print(pc.headline_stats())

#V - I can see that line 14 changes the player
#V - What I don't quite understand is how line 17 chooses what year stats to present



p_cstats = player.PlayerCareer('201938')
print(p_cstats.regular_season_career_totals())


#V - Currently trying to figure out how to
"""
#V - Currently trying to figure out how to to grab a chart of ALL the players so I can pick a specific one
2 - Grab all the players from a certain team
3 - Access the data once it is created, (still trying to understand where files are created and what command creates them)
aldjsl;as
"""
