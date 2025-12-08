"""Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as the letters "d", "o", or "g" don't appear in this order)

Hints:
you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided."""

word = input("Enter the word to find: ").lower()
text = input("Enter the text to search in: ").lower()


for letter in word:
    if letter not in text:
        print("no")
        exit()
    
    #existe
    pos = text.find(letter)
    text = text[pos+1:] #copia a partir da proxima letra
    continue

print("yes")

#index() retorna indice de 1a ocorrencia de arg (ou -1 se nao achar)
#comeca a procurar a 2a letra a partir do indice da 1a letra + 1
