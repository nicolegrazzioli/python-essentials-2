"""The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt
the expected output should look as follows:

Output
a -> 3
b -> 2
c -> 1"""

from os import strerror
import string, unicodedata

# new = {letra: 0 for indice, letra in enumerate(letras)}
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

    new = f + '.hist'
    try:
        with open(new, 'wt') as out:
            for key in sorted(counts, key=counts.get, reverse=True):
                # print(key, "->", new[key])
                linha = f"{key} -> {counts[key]}\n"
                out.write(linha)
            print("file saved: ", new)

    except IOError as e:
        print("error: ", strerror(e.errno))

except IOError as e:
    print("error: ", strerror(e.errno))