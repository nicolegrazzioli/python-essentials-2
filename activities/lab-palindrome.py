text = input("text: ")

if text > 1 and text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")