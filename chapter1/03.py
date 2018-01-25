import re

a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wordCounts = list(map(lambda n:len(re.sub('[,.]', '', n)), a.split()))
print(wordCounts)