def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())

# com argumentos
def make_closure(par):
    loc = par # variavel privada da closure

    def power(p):
        return p ** loc
    return power
    # retorna um 'pacote' com a função power e o valor loc

fsqr = make_closure(2) # 'pacote' com power e loc = 2 (^2)
fcub = make_closure(3) # outro 'pacote' com power e loc = 3 (^3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64

#########
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner

b_tag = tag('<b>')
print(b_tag('Monty Python')) # <b>Monty Python</b>




