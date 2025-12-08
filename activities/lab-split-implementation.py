"""Python Essentials: Split Implementation
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument – a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
Use the template in the editor. Test your code carefully.


Expected output
Output
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
[]
['abc']
[]
"""


#varios espaços conta como 1 so

def mysplit(strng):
    lista = []
    first = end = 0
    
    for i in range(len(strng)):
        if strng[i].isspace():
            # space = strng[i]
            continue
        
        if strng[i].isalpha():
            first = strng[i] #guarda inicio
            end = strng.find(' ', i)
        
            lista.append(strng[i:end])
        
        #se for espaço ultimo eh posicao do el +1?
    return lista


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    