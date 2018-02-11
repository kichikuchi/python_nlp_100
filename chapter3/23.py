import json
import re

f = open('jawiki-country.json')
flist = list(f)

england = ""
for item in flist:
    jsonData = json.loads(item)
    if jsonData["title"] == "イギリス":
        england = jsonData["text"]

lines = england.split('\n')
for line in lines:
    if re.search('==(.)+==', line):
        print(line.replace('=', ''), line.count('=') // 2 - 1)