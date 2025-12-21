# função anonima (não mais - variavel 'two') sem parametros que sempre retorna 2 
two = lambda: 2
# função anonima com 1 parametro que retorna o quadrado do parametro
sqr = lambda x: x * x
# função anonima com 2 parametros que retorna o 1o elevado ao 2o
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# 4 4
# 1 1
# 0 0
# 1 1
# 4 4

###############
def print_function(args, fun): # lista de argumentos e função chamada (quantidade de valores do 1o parametro) vezes
    for x in args:
        print('f(', x,')= ', fun(x), sep='')

# def poly(x):
#     return 2 * x**2 - 4 * x + 2 #f(x) = 2x^2 - 4x + 2

# print_function([x for x in range(-2, 3)], poly)
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# f(-2)= 18
# f(-1)= 8
# f(0)= 2
# f(1)= 0
# f(2)= 2

###############
# MAP + LAMBDA -- map(function, list)
list_1 = [x for x in range(5)] # [0, 1, 2, 3, 4]
list_2 = list(map(lambda x: 2 ** x, list_1)) # [1, 2, 4, 8, 16]
print(list_2) # [1, 2, 4, 8, 16]

for x in map(lambda x: x * x, list_2):
    print(x, end=' ') # 1 4 16 64 256
print()

###############
# FILTER + LAMBDA -- filter(function, list)
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data) # todos
print(filtered) # positivos pares
    
