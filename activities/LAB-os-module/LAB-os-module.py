"""
tree
|--- c
--|--- other_courses
----|--- python
----|--- cpp
|--- cpp
--|--- other_courses
----|--- c
----|--- python
|--- python
--|--- other_courses
----|--- c
----|--- cpp

Example input:
path="./tree", dir="python"

Example output:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python
"""

from os import strerror
import os

# path = caminho relativo ou absoluto de onde inciar a procura
# dir = diretorio que quer achar no path - recursivo (inclui subdiretorios)
def find(path, dir):
    path = os.path.abspath(path)

    if dir in os.listdir(path):
        print(os.path.join(path, dir))
    
    for file in os.listdir(path):
        atual_path = os.path.join(path, file)
        if os.path.isdir(atual_path):
            find(atual_path, dir)


os.chdir("activities/LAB-os-module")
search = input("Path and dir to search (model: 'path dir'): ").split()

try:
    find(search[0], search[1])
except IOError as e:
    print(strerror(e.errno))