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
        # if not c in counts and c.isalpha():
        #     counts.update({c: 1})
        # if c in counts:
        #     counts[c] += 1 

    sorted_counts = dict(sorted(counts.items()))

    for key in sorted_counts.keys():
        print(key, "->", sorted_counts[key])

except IOError as e:
    print("error: ", strerror(e.errno))