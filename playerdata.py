from __future__ import print_function
from nba_py import player

# endpoint currently disabled on stats.nba.com
# pd = player._PlayerDashboard('203507')
# print(pd.starting_position())

ap = player.PlayerList()
print(ap.info())

pc = player.PlayerSummary('203506')
print(pc.headline_stats())

p_cstats = player.PlayerCareer('201938')
print(p_cstats.regular_season_career_totals())
