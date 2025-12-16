# PROCEDURAL
stack = [] #lista vazia

#adicionar elemento - recebe o valor, adiciona no final da lista e não retorna nada
def push(val):
    stack.append(val)

#remover elemento - remove o último elemento da lista e retorna ele
def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop()) #1
print(pop()) #2
print(pop()) #3