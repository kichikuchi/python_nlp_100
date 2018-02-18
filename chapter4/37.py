import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname="ipag.ttf", size=14)

f = open('neko.txt.mecab')

book = []
sentence = []

for line in f:
    if line.count("EOS"):
        book.append(sentence)
        sentence = []
    else:
        surface = line.split("\t")[0]
        morphemes = line.split("\t")[1].split(",")
        base = morphemes[5]
        pos = morphemes[0]
        pos1 = morphemes[1]
        dic = {"surface": surface, "base": base, "pos": pos, "pos1": pos1}
        sentence.append(dic)

dicCount = {}
for i in book:
    for element in i:
        key = element["surface"]
        if key in dicCount.keys():
            dicCount[key]+=1
        else:
            dicCount[key] = 1

sorted = sorted(dicCount.items(), key=lambda x: -x[1])[0:10]
keys = []
values = []

for i in sorted:
    keys.append(i[0])
    values.append(i[1])

x = range(10)
plt.bar(x, values)
plt.xticks(x, keys, fontproperties=fp)
plt.show()