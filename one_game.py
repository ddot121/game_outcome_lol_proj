import cassiopeia as cass
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def getAPI_key():
    f = open("api_key.txt", "r")
    return f.read()

cass.set_riot_api_key(getAPI_key())

adc_list = ["Ezreal", "Jhin", "Kai'Sa", "Vayne", "Lucian",
"Samira", "Kog'Maw", "Jinx", "Miss Fortune", "Twitch",
"Tristana", "Ashe", "Swain", "Caitlyn", "Xayah",
"Seraphine", "Draven", "Kalista", "Sivir", "Karthus",
"Varus", "Veigar", "Aphelios", "Ziggs", "Zeri", "Heimerdinger",
"Yasuo"]

supp_list = ["Seraphine", "Rell", "Morgana", "Yuumi", "Lulu",
"Senna", "Lux", "Swain", "Pyke", "Sona", "Brand", "Thresh", "Soraka",
"Nami", "Bard", "Vel'Koz", "Xerath", "Blitzcrank", "Zyra", "Zilean", 
"Pantheon", "Nautilus", "Leona", "Taric", "Alistar", "Rakan", "Karma",
"Braum", "Renata Glasc", "Janna", "Maokai", "Shaco", "Sett", "Galio", "Malphite", "Gragas"]

summoner = cass.Summoner(name= 'ddot', region= 'EUW')
puuid = cass.get_summoner(name= 'ddot', region= "EUW").puuid
game_one = cass.get_match_history(continent= 'EUROPE', region= 'EUW', puuid= puuid)[0]
champions = [p.champion.name for p in game_one.participants]
bot_lane = [champ for champ in champions if champ in adc_list or champ in supp_list] # disadv: off-meta picks are not included

players = [game_one.participants]
first_player = players[0]
# first_player
# print(game_one.red_team.bans)


# for p in game_one.participants:
#         print(p.champion.name)
# print(players)
# for p in game_one.participants:
#     print(
#             p.summoner.region,
#             p.summoner.account_id,
#             p.summoner.name,
#             p.summoner.id,
#             p.champion.id,
#             p.stats.win,
#             p.runes.keystone.name,
#         )




# champion_id_to_name_mapping = {
#         champion.id: champion.name for champion in cass.get_champions(region="EUW")
# #     }
# print(champion_id_to_name_mapping)