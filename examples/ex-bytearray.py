data = bytearray(10) # 10 bytes '0'

for i in range(len(data)):
    data[i] = 10 - i

try:
    bf = open('files/file.bin', 'wb') #'wb' = write binary
    bf.write(data)
    bf.close()

    bf = open('files/file.bin', 'rb') #'rb' = read binary
    bf.readinto(data) # le o conteudo para o byteaaray 'data'
    bf.close()

    for b in data:
        print(hex(b), end=' ') # 0xa 0x9 0x8 0x7 0x6 0x5 0x4 0x3 0x2 0x1
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# OU READ() -- se tiver certeza que o arquivo cabe na memória, ou delimita bytes para ler (argumento)
from os import strerror

try:
    bf = open('files/file.bin', 'rb')
    data = bytearray(bf.read(5)) # 0xa 0x9 0x8 0x7 0x6 
    bf.close()

    for b in data:
        print(hex(b), end=' ') 
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))