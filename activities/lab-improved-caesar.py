"""You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Test Data
Sample input:

abcxyzABCxyz 123
2

Sample output:

cdezabCDEzab 123"""

#ord(char) \ chr(int)
text = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
while shift < 1 or shift > 25:
    shift = int(input("Invalid shift. Please enter a value between 1 and 25: "))

cipher = '' #string vazia 
for c in text:
    if not c.isalpha():
        cipher += c
        continue #proximo

    new = ord(c) + shift #novo ascii

    if c.islower():
        if new > ord('z'):
            new = ord('a') + (new - ord('z') - 1) #quantas letras passou do z - 1 ('z' foi o ultimo valido, começa do 'a')
    else:
        if new > ord('Z'):
            new = ord('A') + (new - ord('Z') - 1)

    cipher += chr(new)
    # print(cipher)


print(cipher)
    