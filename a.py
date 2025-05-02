from data import stats

playerIdsToName = {}

for i in stats:
    if i["playerid"] in playerIdsToName:
        continue
    playerIdsToName[i["playerid"]] = {
        "name": i["playername"],
        "goals": 0,
        "assists": 0,
        "yellow_cards": 0,
        "red_cards": 0,
        "save": 0,
        "MOTMs": 0,
        "appearances": 0,
    }

for i in stats:
    obj = playerIdsToName[i["playerid"]]
    obj["goals"] += i["goals"]
    obj["assists"] += i["assists"]
    obj["appearances"] += i["appearances"]
    obj["MOTMs"] += i["MOTMs"]
    obj["yellow_cards"] += i["yellow_cards"]
    obj["red_cards"] += i["red_cards"] + i["two_yellow"]


f = open("a.json","+w")
import json
f.write(json.dumps(playerIdsToName))
f.close()