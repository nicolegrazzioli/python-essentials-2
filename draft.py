from os import strerror

try:
	file = open('newtext.txt', 'wt') 
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
	
	arq = open('newtext.txt', 'rt')
	s = arq.read()
	for c in s:
		print(c, end='')
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    
