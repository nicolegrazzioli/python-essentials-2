errno.EACCES # permissão negada (ex: tentar escrever em um arquivo de leitura)
errno.EBADF # arquivo inválido (ex: usar um descritor de arquivo fechado)
errno.EEXIST # arquivo já existe (ex: tentar criar um arquivo que já existe)
errno.EFBIG # arquivo muito grande (ex: tentar criar um arquivo maior que o SO permite)
errno.EISDIR # é um diretório (ex: tentar escrever em um diretório como se fosse um arquivo)
errno.EMFILE # muitos arquivos abertos (ex: tentar abrir mais arquivos do que o limite do SO)
errno.ENOENT # arquivo ou diretório não encontrado (ex: tentar abrir um arquivo que não existe)
errno.ENOSPC # sem espaço em disco (ex: tentar escrever em um disco cheio)

# uso
from os import strerror

try:
    s = open("files/newtext.txt", "rt")
    # ...
    s.close()
except Exception as exc:
    print("The file could not be opened: ", strerror(exc.errno)) 
    # strerror(number) -- retorna uma string descrevendo o erro
    # if exc.errno == errno.ENOENT:
    #     print("The file doesn't exist.")
    # elif exc.errno == errno.EMFILE:
    #     print("You've opened too many files.")
    # else:
    #     print("The error number is:", exc.errno)
  