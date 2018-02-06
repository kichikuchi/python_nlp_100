col1 = open('col1.txt')
col2 = open('col2.txt')
newFile = open('merge.txt', 'w')

array1 = list(col1)
array2 = list(col2)

for i in range(len(array1)):
    newFile.write(array1[i].replace("\n", ""))
    newFile.write("\t")
    newFile.write(array2[i])