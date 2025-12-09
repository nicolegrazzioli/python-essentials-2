"""As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

Test Data
Sample input:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:

Yes


Sample input:

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:

No"""

size = 9

text = input("Enter Sudoku rows: ").replace('\n', '')
if len(text) != size * size or not text.isdigit() or '0' in text:
    print("No")
    exit()

sudoku = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(int(text[i * size + j]))
    sudoku.append(row)

# linhas ok
for row in sudoku:
    copy = sorted(row)
    # print(f"linha = {row}\tordenado = {copy}")
    if copy != list(range(1, 10)):
        print("No")
        exit()
        
# colunas ok
for j in range(size):
    col = []
    for i in range(size):
        col.append(sudoku[i][j]) #extrai coluna
    copy2 = sorted(col)
    # print(f"coluna = {col}\tordenado = {copy2}")
    if copy2 != list(range(1, 10)):
        print("No")
        exit()

# 3x3
for box_row in range(3): #blocos de altura
    for box_col in range(3): #blocos de largura
        box = [] #lista vazia
        for i in range(3): #linhas do bloco
            for j in range(3): #colunas do bloco
                #indice da linha = box_row * 3 + i
                #indice da coluna = box_col * 3 + j
                #digito adicionado a lista box
                box.append(sudoku[box_row * 3 + i][box_col * 3 + j])
        copy3 = sorted(box)
        # print(f"box = {box}\tordenado = {copy3}")
        if copy3 != list(range(1, 10)):
            print("No")
            exit()

print("Yes")