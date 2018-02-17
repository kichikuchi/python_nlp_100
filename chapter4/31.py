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

for i in book:
    for ii in i:
        if ii["pos"] == "動詞":
            print(ii["surface"])