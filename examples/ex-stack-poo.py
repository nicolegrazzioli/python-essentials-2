class Stack:
    # implementa uma lista em cada objeto, escondida dos usuários da classe
    # propriedades adcionadas nas classes manualmente

    # função construtor - construir um novo objeto, chamada automaticamente
    def __init__(self): #1+ parametros (objeto)
        # self.stack_list = [] #nova propriedade de objeto: lista vazia para pilha
        self.__stack_list = [] #nova propriedade 'privada' do objeto

    def push(self, val): #1+ parametros (objeto, valor)
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object1 = Stack()  # cria objeto 
stack_object2 = Stack() 
# nome_objeto.propriedade - sem () pq não é um método/função
# print(len(stack_obj.stack_list))  # 0
# print(len(stack_obj.__stack_list))  # AttributeError: 'Stack' object has no attribute 'stack_list'
stack_object1.push(3)
stack_object2.push(stack_object1.pop())
stack_object1.push(1)

print(stack_object1.pop()) #1
print(stack_object2.pop()) #2



# nova SUB CLASSE: soma dos elementos armazenados na pilha
class AddingStack(Stack): #herda de Stack
    def __init__(self):
        #Super.construtor(self) - para invocar metodo dentro da classe precisa do self
        Stack.__init__(self) #chama o construtor da super classe
        self.__sum = 0 #privada
    
    def push(self, val):
        self.__sum += val #incrementa 'sum' da classe atual (sub)
        Stack.push(self, val) #chama o metodo push da super classe

    def pop(self):
        val = Stack.pop(self) #metodo da super classe
        self.__sum -= val #tira valor recebido (val)
        return val
    
    #mostrar valor de soma mesmo protegido
    def get_sum(self):
        return self.__sum

stack_add = AddingStack()
for i in range(5):
    stack_add.push(i)  #0,1,2,3,4
print(stack_add.get_sum())  #10

for i in range(5):
    print(stack_add.pop())  #4,3,2,1,0