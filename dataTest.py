import json

with open("data.json", "r", encoding="utf-8") as dataFile:
    data = json.load(dataFile)
    print(data["perks"]["Gun Fu"]["description"]) #THIS WORKS