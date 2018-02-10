text = open('hightemp.txt')
textArray = list(text)
new = []
for text in textArray:
    new.append(text.split("\t"))

sorted = sorted(new, key=lambda data: data[2])

result = []
for item in sorted:
    result.append('\t'.join(item))

print(''.join(result))