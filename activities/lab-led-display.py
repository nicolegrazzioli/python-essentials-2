"""Python Essentials 2: LED Display
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful"""

digits = [ '1111110',  	# 0
      # ABCDEFG
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]

# matriz(linha = 5, coluna = 3)
# A: Topo (meio cima) = 0 = (0,0), (0,1), (0,2)
# B: Superior Direito = 1 = (0, 2), (1,2), (2,2)
# C: Inferior Direito = 2 = (2,2), (3,2), (4,2)
# D: Base (meio baixo) = 3 = (4,0), (4,1), (4,2)
# E: Inferior Esquerdo = 4 = (2,0), (3,0), (4,0)
# F: Superior Esquerdo = 5 = (0,0), (1,0), (2,0)
# G: Meio (meio meio) = 6 = (2,0), (2,1), (2,2)

def print_number(num): #matriz 5x3
    global total
    linhas = ['' for _ in range(5)]
    digits_str = str(num)

    #cada digito do numero digitado
    for d in digits_str:
        #matriz 5x3 temporaria (1 digito)
        segs = [[' ' for _ in range(3)] for _ in range(5)]
        pos = ord(d) - ord('0') #posição do digito na lista digits

        #string binaria do digito
        ptrn = digits[pos]

        #bits (a-g) para linha x coluna + preenche matriz 5x3
        if ptrn[0] == '1': #A
            segs[0][0] = segs[0][1] = segs[0][2] = '#'
        if ptrn[1] == '1': #B
            segs[0][2] = segs[1][2] = segs[2][2] = '#'
        if ptrn[2] == '1': #C
            segs[2][2] = segs[3][2] = segs[4][2] = '#'
        if ptrn[3] == '1': #D
            segs[4][0] = segs[4][1] = segs[4][2] = '#'
        if ptrn[4] == '1': #E
            segs[2][0] = segs[3][0] = segs[4][0] = '#'
        if ptrn[5] == '1': #F
            segs[0][0] = segs[1][0] = segs[2][0] = '#'
        if ptrn[6] == '1': #G
            segs[2][0] = segs[2][1] = segs[2][2] = '#'
        
        #anexa matriz 5x3 na horizontal
        for lin in range(5):
            #junta os 3 caracteres da linha atual de segs + anexa em linhas com espaço ' '
            linhas[lin] += ''.join(segs[lin]) + ' '
    
    #imprime tudo (\n automatica)
    for lin in linhas:
        print(lin)

print_number(int(input("Enter the number you wish to display: ")))
    