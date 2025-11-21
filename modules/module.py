print("I like to be a module.")
print(__name__)

#!/usr/bin/env python3 
# para SOs Unix (mac, linux) essa linha informa onde está o interpretador Python (como executar o conteúdo)
# em SOs Windows essa linha é ignorada

#doc-string: string posta antes de qualquer instrução de módulo, explica o conteúdo do módulo
#"" module.py - an example of a Python module ""

__counter = 0

# funções podem ser importadas
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
  


