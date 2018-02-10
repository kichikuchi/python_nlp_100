text = open('hightemp.txt')
textArray = list(text)

col1 = []
for text in textArray:
    col1.append(text.split("\t")[0])

uniq = set(col1)
print(uniq)