text = open('col1.txt')
textArray = list(text)

input = input("Plase Enter the number.")

for i in reversed(range(int(input))):
    print(textArray[len(textArray) - 1 - i])