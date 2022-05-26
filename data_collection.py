import random
import cassiopeia as cass
from itertools import product
import sys
import csv

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

def getGoldPlayers(division):
    """Retrieve 81 players (only 81 fit on one page) in Gold x, where x is the specified division
    e.g. GOLD IV, GOLD III..."""

    players = []
    y = cass.get_paginated_league_entries(queue= cass.Queue.ranked_solo_fives, tier= "GOLD", division= division, region= "EUW")
    for entry in y[:81]:
        players.append(entry.summoner.sanitized_name)
            
    return players

def getTierPlayers(tier, division):
    """Retrieve 81 players (only 81 fit on one page) in given tier x, where x is the specified division
    e.g. GOLD IV, SILVER II..."""

    players = []
    y = cass.get_paginated_league_entries(queue= cass.Queue.ranked_solo_fives, tier= tier, division= division, region= "EUW")
    try:    
        for entry in y[:50]:
            players.append(entry.summoner.sanitized_name)
    except UnicodeEncodeError:
        pass
            
    return players

cass.set_riot_api_key(getAPI_key())  # This overrides the value set in your configuration/settings.


tiers = ["SILVER", "GOLD"]
divisions = ["IV", "III", "II", "I"]

headers = ["Summoner", "Tier", "Division"]

with open("summoners.csv", "w", encoding="UTF8", newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

    for rank in product(tiers, divisions):
        x = getTierPlayers(tier= rank[0], division= rank[1])
        for name in x:
            writer.writerow([name, rank[0], rank[1]])

