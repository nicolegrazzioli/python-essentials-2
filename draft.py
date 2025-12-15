class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
        self.other()

    def other(self):
        print("other")
  
obj = Classy()
obj.var = 3
obj.method()

# 2 3 
# other

######################
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible() # visible

try:
    obj.__hidden()
except:
    print("failed") # failed

obj._Classy__hidden() # hidden

(obj.__module__)

#################
class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne) # ( object )
printBases(SuperTwo) # ( object )
printBases(Sub) # ( SuperOne SuperTwo )

#####################
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys(): #busca nomes dos atributos
        if name.startswith('i'):
            val = getattr(obj, name) #pega valor atual
            if isinstance(val, int): #verifica se é do tipo integer
                setattr(obj, name, val + 1) #(objeto, atributo, novo valor)

print(obj.__dict__)
# {'a': 1, 'integer': 4, 'b': 2, 'i': 3, 'z': 5, 'ireal': 3.5}
incIntsI(obj)
print(obj.__dict__)
# {'a': 1, 'integer': 5, 'b': 2, 'i': 4, 'z': 5, 'ireal': 3.5}

##########################
class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)

obj = Sample()
obj.myself()
# My name is Sample living in a __main__
