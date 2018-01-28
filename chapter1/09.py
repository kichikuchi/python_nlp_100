import re
import random

a = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = list(filter(lambda n: len(n) > 0, map(lambda n:re.sub('[,.]', '', n), a.split())))

result = []
for word in words:
    if len(word) < 5:
        result.append(word)
    else:
        first = word[0]
        last = word[-1]
        middleList = list(word[1:-1])
        random.shuffle(middleList)
        middle = ''.join(middleList)
        result.append(first + middle + last)

print(result)