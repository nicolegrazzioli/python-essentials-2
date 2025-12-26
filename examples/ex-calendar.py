import calendar

# CALENDARIO DE ANO
print(calendar.calendar(2025))
calendar.prcal(2025) #nao precisa print()
# w = date column width (default 2)
# l = linhas por semana (default 1)
# c = espaços entre colunas de meses (default 6)
# m = qtd de colunas (default 3)


# CALENDARIO DE MES ESPECIFICO
print(calendar.month(2025, 12))
calendar.prmonth(2025, 12) #nao precisa print()
# w = date column width (default 2)
# l = linhas por semana (default 1)


# MUDAR 1o DIA DA SEMANA
calendar.setfirstweekday(calendar.SUNDAY) #6
print(calendar.month(2025, 12))


# INT DIA DA SEMANA
print(calendar.weekday(2025, 12, 26)) #4 = quarta feira


# HEADER MAIOR (até 3)
print(calendar.weekheader(2)) # Mo Tu We Th Fr Sa Su
print(calendar.weekheader(4)) # Mon  Tue  Wed  Thu  Fri  Sat  Sun 