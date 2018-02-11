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
    if re.search('ファイル:', line):
        m = re.search('ファイル:(.+)(.jpg|.JPG|.jpeg|.JPEG|.svg)', line)
        print(m[0][5:])
        