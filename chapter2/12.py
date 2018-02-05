f = open('hightemp.txt')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for line in f:
    col1.write(line.split("\t")[0])
    col1.write('\n')
    col2.write(line.split("\t")[1])
    col2.write('\n')

f.close()
col1.close()
col2.close()