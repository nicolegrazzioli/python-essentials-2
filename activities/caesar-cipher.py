# Caesar cipher - apenas letras em latim, tudo maiusculo
text = input("Enter your message: ")
cipher = '' #string vazia
for char in text:
    if not char.isalpha():
        continue
    char = char.upper() #sempre converte para maiusculo
    code = ord(char) + 1 #pega o codigo ascii + 1 (proxima)
        #DES = ord(char) - 1
    if code > ord('Z'): #se passar de Z, volta para A
        #DES = if code < ord('A'):
        code = ord('A')
            #DES = ord('Z)
    cipher += chr(code) #converte de volta para char e adiciona na string

print(cipher)
    