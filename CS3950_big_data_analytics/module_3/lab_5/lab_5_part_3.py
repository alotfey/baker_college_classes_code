"""Lab 5 Part 3: NBA Player Data Analysis"""

import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

player_dict = players.get_players()

# Use ternary operator or write function
# Names are case sensitive
bron = [player for player in player_dict if player["full_name"] == "LeBron James"][0]
bron_id = bron["id"]
# find team Ids
from nba_api.stats.static import teams

teams = teams.get_teams()
GSW = [x for x in teams if x["full_name"] == "Golden State Warriors"][0]
GSW_id = GSW["id"]
print(f"LeBron James ID: {bron_id}")
print(f"GSW Team ID: {GSW_id}")

gamelog = playergamelog.PlayerGameLog(player_id=bron_id, season="2023")
df = gamelog.get_data_frames()[0]
print(df.SEASON_ID.unique())

df.to_csv("lebron_james_2023_games.CSV", index=False)

print(df.head())
