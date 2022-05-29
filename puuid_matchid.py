import cassiopeia as cass
import sys
import pandas as pd

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

def getPUUID(summoner):
    """Retrieve PUUID of summoner"""
    try:
        return cass.get_summoner(name= summoner, region= "EUW").puuid
    except AttributeError:
        print(summoner)

def getMATCHID(puuid):
    """Retrieve match history of summoner given PUUID. Returns match ids of last 20 games"""
    try:
        return cass.get_match_history(continent= 'EUROPE', region= 'EUW', puuid= puuid)
    except AttributeError:
        print(puuid)


cass.set_riot_api_key(getAPI_key())

summoners = pd.read_csv("low_elo_summoners.csv")

puuid = [getPUUID(summoner) for indx, summoner in enumerate(summoners.Summoner)] # puuid of each summoner
matchid = [getMATCHID(summoner) for indx, summoner in enumerate(summoners.Summoner)] # matchid of each summoner

summoners['PUUID'] = puuid
summoners['MATCHID'] = matchid

summoners.to_csv("low_elo_summoners_puuid.csv", index= False)
