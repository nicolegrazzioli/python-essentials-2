"""
- codigo 2 letras (país)
- 2 digitos para checar validade
- numero da conta (até 30 caracteres alfanumericos)
Validar
- verifica se o tamanho está correto (pelo país)
- move os 4 primeiros caracteres (país e checagem) para o final da string
- converte letras em numeros (A=10, B=11,... Z=35)
- pega o numero inteiro resultante e calcula o resto da divisão por 97 -> se o resto = 1, é válido
"""

iban = input("IBAN: ").replace(' ', '').upper()

if not iban.isalnum() or len(iban) < 4 or len(iban) > 34:
    print("Invalid IBAN format.")
    exit()

iban = iban[4:] + iban[:4] #move os 4 primeiros caracteres para o final
converted_iban = ''
for char in iban:
    if char.isdigit():
        converted_iban += char
    else:
        converted_iban += str(ord(char) - ord('A') + 10) #converte letra em numero
iban = int(converted_iban)
if iban % 97 == 1:
    print("IBAN entered is valid.")
else:
    print("IBAN entered is invalid.")