
import json
'''
with open("data.json", "r", encoding="utf-8") as dataFile:
    data = json.load(dataFile)
    print(data["perks"]["Gun Fu"]["description"]) #THIS WORKS

inp = input("Input 1: ")
print(inp, type(inp))
inp = int(input("Input 2: "))
print(inp, type(inp))
'''
with open('template.json', 'r', encoding='utf-8') as dataFile:
    data = json.load(dataFile)
#    data = str(data)
    print(json.dumps(data, indent=1))