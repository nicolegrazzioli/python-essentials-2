from modules.module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

from sys import path 
path.append('C:\\Users\\user\\py\\modules') #ou insert()
for p in path:
  print(p)


