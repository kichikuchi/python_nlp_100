def cipher(characters):
    a = []
    for character in characters:
        if character.islower():
            ascii = ord(character)
            a.append(chr(219 - ascii))
        else:
            a.append(character)
    
    return ''.join(a)

a = "Hoge Fuga PiYo"
encryption = cipher(a)
decryption = cipher(encryption)
print("original: ", a)
print("encryption: ", encryption)
print("decryption: ", decryption)