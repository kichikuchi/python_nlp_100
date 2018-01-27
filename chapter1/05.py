a = "I am an NLPer"
words = a.split()

def ngram(array, n):
    result = []

    while len(array) > 0:
        result.append(''.join(array[0:n]))
        del array[0:n]
    
    print(result)

print("characters")
ngram(list(a), 2)

print("words")
ngram(words, 2)
    
