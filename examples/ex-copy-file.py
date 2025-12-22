from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb') # leitura
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno) # termina execuçao com mensagem de codigo de erro	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

# area de transferencia = BUFFER
buffer = bytearray(65536) # prepara uma parte da memoria (64kb) para transferir os dados da origem para o destino
# maior = mais rapido copiando e menos operações I/O

total  = 0 # contar bytes copiados
try:
    readin = src.readinto(buffer) # tenta encher o buffer pela 1a vez

    # enquanto recebe um valor > 0 de bytes, repete
    while readin > 0: 
        written = dst.write(buffer[:readin]) # escreve o conteudo do buffer no destino (bytes limitados)
        total += written # atualiza contador
        readin = src.readinto(buffer) # le o proximo bloco do arquivo

except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()
    