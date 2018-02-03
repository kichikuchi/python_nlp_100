f = open('hightemp.txt')

for line in f:
    line = line.replace('\t', ' ')
    print(line)