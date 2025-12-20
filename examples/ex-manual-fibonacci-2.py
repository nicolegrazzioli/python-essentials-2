# classe iterador - calcula os numeros conforme solicitados
class Fib: 
    def __init__(self, nn):
        self.__n = nn # limite
        self.__i = 0 # contador (atual)
        self.__p1 = self.__p2 = 1 # define os 1os 2 numeros

    def __iter__(self): # permite que o objeto seja iterado
        print("Fib iter")
        return self

    def __next__(self): # gera o proximo valor
        self.__i += 1 # incrementa contador
        if self.__i > self.__n: # se chegou ao fim
            raise StopIteration # para
        if self.__i in [1, 2]: # se for 1o ou 2o numero
            return 1
        # atualiza: 2o vira 1o e novo vira 2o
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

# objeto iteravel que usa o iterador Fib
class Class:
    def __init__(self, n): # recebe tamanho n
        self.__iter = Fib(n) # cria uma instancia de Fib (delega os calculos)

    def __iter__(self): # metodo chamado pelo for
        print("Class iter")
        return self.__iter # retorna o objeto (iterador) Fib


object = Class(8)

for i in object:
    print(i)

# Class iter -- for recebe objeto Fib
# 1 -- Fib.__next__
# 1
# 2
# 3
# 5
# 8
# 13
# 21