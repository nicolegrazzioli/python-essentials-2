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

os.chdir("activities/LAB-os-module")
# print("1st cwd = ", os.getcwd())

# path = caminho relativo ou absoluto de onde inciar a procura
# dir = diretorio que quer achar no path - recursivo (inclui subdiretorios)
# imprimr path absoluto
# if dir in sei la o que
def find(path, dir):
    print(f"path = {path}, dir = {dir}")
    os.chdir(path) #achou
    # print(os.getcwd())
    if dir in os.listdir():
        print(os.getcwd() + '\\' + dir)

search = input("Path and dir to search (model: 'path dir'): ").split()

try:
    find(search[0], search[1])
except IOError as e:
    print(strerror(e.errno))