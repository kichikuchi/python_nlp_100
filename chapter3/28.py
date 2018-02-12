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

for k, v in dic.items():
    print(k,":", v)