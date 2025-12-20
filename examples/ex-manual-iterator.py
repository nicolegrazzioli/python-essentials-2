class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    # chamado quando o for começa, retorna o objeto iterador
    def __iter__(self):
        return self

    # chamado a cada iteração para obter o próximo valor
    def __next__(self):
        # verifica se ja foi todos os caracteres
        if self.i == len(self.s):
            raise StopIteration # acabou o for
        v = self.s[self.i] # aumenta contador
        self.i += 1
        return v


for x in I():
    print(x,end='') # abc
    # I() cria instancia da classe com s = 'abc' e i = 0
    # for chama I.__iter__() para obter o iterador (self)
    # for chama I.__next__() para atualizar o indice
    # termina o loop com StopIteration quando i == len(s)
