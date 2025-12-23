"""A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt
the expected output should look as follows:

Output
a -> 1
b -> 1
c -> 1"""

from os import strerror
import string, unicodedata

# counts = {letra: 0 for indice, letra in enumerate(letras)}
counts = {}

f = input("name of the file (files/histogram.txt): ")

try:
    file = open(f, 'rt')
    stream = file.read()

    stream = unicodedata.normalize('NFD', stream) # separa acentos etc

    for c in stream:
        c = c.lower()

        if c in string.ascii_lowercase:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1

    sorted_counts = dict(sorted(counts.items()))

    for key, value in sorted_counts.items():
        print(key, "->", value)

except IOError as e:
    print("error: ", strerror(e.errno))