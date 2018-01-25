a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = a.split()
dict = {}
for i, c in enumerate(words):
    if (i+1) in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict.update({(i+1):c[0:1]})
    else:
        dict.update({(i+1):c[0:2]})

print(dict)