text = open('col1.txt')
textArray = list(text)

input = input("Plase Enter the number.")

for i in range(0, int(input)):
    print(textArray[i])