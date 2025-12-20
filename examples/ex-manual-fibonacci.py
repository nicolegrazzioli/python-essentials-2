class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn # limite
        self.__i = 0 # numero atual (contador)
        self.__p1 = self.__p2 = 1 # 2 numeros anteriores

    def __iter__(self):
        print("__iter__")
        return self # retorna o proprio iterador

    def __next__(self): # cria a sequencia
        print("__next__") # printa
        self.__i += 1 # atualiza contador
        if self.__i > self.__n: # fim da sequencia
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

# iterar pelos primeiros n valores de fibonacci
for i in Fib(10):
    print(i)

# __init__ -- objeto iterador instanciado
# __iter__ -- acessa iterador
# __next__
# 1
# __next__
# 1
# __next__
# 2
# __next__
# 3
# __next__
# 5
# __next__
# 8
# __next__
# 13
# __next__
# 21
# __next__
# 34
# __next__
# 55
# __next__ -- termina