a = "I am an NLPer"
words = a.split()

def ngram(array, n):
    result = []

    while len(array) > (n - 1):
        result.append(''.join(array[0:n]))
        del array[0:1]
    
    print(result)

print("characters")
ngram(list(a), 2)

print("words")
ngram(words, 2)
    
