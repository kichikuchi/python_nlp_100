class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos

f = open('neko.txt.cabocha')

book = []
sentence = []

for line in f:
    if line.count("EOS"):
        book.append(sentence)
        sentence = []
    else:
        if line[0] == "*":
            continue
        surface = line.split("\t")[0]
        morphemes = line.split("\t")[1].split(",")
        base = morphemes[6]
        pos = morphemes[0]
        pos1 = morphemes[1]
        morph = Morph(surface, base, pos, pos1)
        sentence.append(morph)

line3 = book[2]
for i in line3:
    print(i.surface)