import os, platform
# print(platform.uname()) #uname_result(system='Windows', node='WIN-F0FOK76J0KO', release='11', version='10.0.26200', machine='AMD64')
# os.mkdir("files/my_1st_directory") #path (endereço)
# print(os.listdir()) #lista diretorios = ['.git', 'activities', 'draft.py', 'examples', 'files', 'modules', 'packages', 'progs', 'README.md', '__pycache__']

# todos os diretorios do path serão criados
# Unix: mkdir -p my_first_directory/my_second_directory
# Windows: mkdir my_first_directory/my_second_directory
# os.makedirs("files/my_1st_directory/my_2nd_directory")
# os.chdir("files/my_1st_directory")
# print(os.listdir()) # ['my_2nd_directory']
print(os.getcwd()) #C:\Users\nicol\nicolegrazzioli\python-essentials-2

# os.rmdir("files/my_1st_directory/my_2nd_directory")
# os.chdir("files/my_1st_directory")
# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir()) # []
print(os.system("mkdir my_first_directory")) #Já existe uma subpasta ou um arquivo my_first_directory. 1

