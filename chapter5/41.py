class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

f = open('neko.txt.cabocha')

book = []
sentence = []
chunk = Chunk()

for line in f:
    if line.count("EOS"):
        sentence.append(chunk)
        chunk = Chunk()
        for i, c in enumerate(sentence):
            for i2, c2 in enumerate(sentence):
                if c2.dst == i:
                    c.srcs.append(i2)

        book.append(sentence)
        sentence = []
    else:
        if line[0] == "*":
            if len(chunk.morphs) > 0:
                sentence.append(chunk)
            chunk = Chunk()
            chunk.dst = int(line.split(" ")[2].replace("D", ""))
        else:
            surface = line.split("\t")[0]
            morphemes = line.split("\t")[1].split(",")
            base = morphemes[6]
            pos = morphemes[0]
            pos1 = morphemes[1]
            morph = Morph(surface, base, pos, pos1)
            chunk.morphs.append(morph)

line3 = book[7]
for c in line3:
    ll = ""
    for m in c.morphs:
        ll += m.surface
    
    print(c.dst, ll, c.srcs)