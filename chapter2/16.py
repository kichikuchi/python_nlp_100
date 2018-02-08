text = open('hightemp.txt')
textArray = list(text)

input = input("Plase Enter the number.")
lineCount = len(textArray) // int(input)

divideList = [textArray[i:i+lineCount] for i in range(0, len(textArray), lineCount)]

for i in range(0, len(divideList)):
    result = open('a{}.txt'.format(i), 'w')
    for line in divideList[i]:
        result.write(line)