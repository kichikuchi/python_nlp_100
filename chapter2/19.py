from collections import Counter

text = open('hightemp.txt')
textArray = list(text)
new = []
col1 = []
for text in textArray:
    new.append(text.split("\t"))
    col1.append(text.split("\t")[0])

counter = Counter(col1)
order = []
for word, cnt in counter.most_common():
    order.append(word)

sorted = sorted(new, key=lambda data: order.index(data[0]))
result = []
for item in sorted:
    result.append('\t'.join(item))

print(''.join(result))