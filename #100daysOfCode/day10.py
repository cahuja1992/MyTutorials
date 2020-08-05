def caesarCipherEncryptor(string, key):
    return "".join([chr((ord(ch) + key - 97) % 26 + 97) for ch in string])
     
string = "xyz"

key = 2
caesarCipherEncryptor(string, key)
