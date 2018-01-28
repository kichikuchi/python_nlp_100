a = "paraparaparadise"
b = "paragraph"

def ngram(array, n):
    result = []

    while len(array) > (n - 1):
        result.append(''.join(array[0:n]))
        del array[0:1]
    
    return result

X = set(ngram(list(a), 2))
Y = set(ngram(list(b), 2))

print("intersection: ", X & Y)
print("diff: ", X ^ Y)
print("union: ", X | Y)

print("X has 'se'?: ", {"se"} <= X)
print("Y has 'se'?: ", {"se"} <= Y)
