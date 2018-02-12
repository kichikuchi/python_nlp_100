import json
import re
import requests

f = open('jawiki-country.json')
flist = list(f)

england = ""
for item in flist:
    jsonData = json.loads(item)
    if jsonData["title"] == "イギリス":
        england = jsonData["text"]

lines = england.split('\n')
flag = False

dic = {}
for line in lines:
    if flag:
        if re.search('\|(.+) \=', line):
            m = re.search('\|(.+) \=', line)
            key = line[m.start():m.end()]
            key = key[1:-2]
            value = line[m.end():]
            value = value.replace('\'\'\'', '')
            
            if re.search('\[\[(.+)\]\]', value):
                value = value.replace('[', '')
                value = value.replace(']', '')

            value = re.sub('<ref(.+)\/>', '', value)
            value = re.sub('<ref(.+)<\/ref>', '', value)
            value = re.sub('<br />', '', value)

            dic[key] = value

    if re.search('\{\{基礎情報', line):
        flag = True
    
    if re.search('^\}\}$', line):
        flag = False

eFlag = dic["国旗画像"]
res = requests.get(f'https://commons.wikimedia.org/w/api.php?action=query&titles=File:{eFlag}&prop=imageinfo&iiprop=url&format=json')
print(res.json()["query"]["pages"]["347935"]["imageinfo"][0]["url"])