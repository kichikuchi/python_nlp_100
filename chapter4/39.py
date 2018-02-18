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

sorted = sorted(dicCount.items(), key=lambda x: -x[1])
keys = []
values = []

for i in sorted:
    keys.append(i[0])
    values.append(i[1])

li_uniq = list(set(values))
li_uniq.sort()
li_uniq.reverse()

x = []
y = []
for (index, count) in enumerate(li_uniq):
    x.append(index+1)
    y.append(count)

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.plot(x, y)
plt.show()