import calendar

# # CALENDARIO DE ANO
# print(calendar.calendar(2025))
# calendar.prcal(2025) #nao precisa print()
# # w = date column width (default 2)
# # l = linhas por semana (default 1)
# # c = espaços entre colunas de meses (default 6)
# # m = qtd de colunas (default 3)


# # CALENDARIO DE MES ESPECIFICO
# print(calendar.month(2025, 12))
# calendar.prmonth(2025, 12) #nao precisa print()
# # w = date column width (default 2)
# # l = linhas por semana (default 1)


# # MUDAR 1o DIA DA SEMANA
# calendar.setfirstweekday(calendar.SUNDAY) #6
# print(calendar.month(2025, 12))


# # INT DIA DA SEMANA
# print(calendar.weekday(2025, 12, 26)) #4 = quarta feira


# # HEADER MAIOR (até 3)
# print(calendar.weekheader(2)) # Mo Tu We Th Fr Sa Su
# print(calendar.weekheader(4)) # Mon  Tue  Wed  Thu  Fri  Sat  Sun 


# # ANO BISSEXTO
# print(calendar.isleap(2020)) # True
# print(calendar.leapdays(2010, 2021)) # 3


# OBJETO CALENDAR 
c = calendar.Calendar(calendar.SUNDAY) # começa semana no domingo

for weekday in c.iterweekdays():
    print(weekday, end=" ") # 6 0 1 2 3 4 5

for date in c.itermonthdates(2019, 11):
    print(date, end=" ") # 2019-10-28 2019-10-29 2019-10-30 2019-10-31 ...

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ") # 4 5 6 7 8 9 10 11 ...

print("\n\ndays2\n") # dia do mes, dia da semana
for i in c.itermonthdays2(2019, 11):
    print(i, end='') # (0, 6)(0, 0)(0, 1)(0, 2)(0, 3)(1, 4)(2, 5)(3, 6) ...

print("\n\ndays3\n") # ano, mes, dia do mes
for i in c.itermonthdays3(2019, 11):
    print(i, end='') # (2019, 10, 27)(2019, 10, 28)(2019, 10, 29) ...

print("\n\ndays4\n") # ano, mes, dia do mes, dia da semana
for i in c.itermonthdays4(2019, 11):
    print(i, end='') # (2019, 10, 27, 6)(2019, 10, 28, 0)(2019, 10, 29, 1) ...

for data in c.monthdays2calendar(2020, 12):
    print(data) # [(6, 6), (7, 0), (8, 1), (9, 2), (10, 3), (11, 4), (12, 5)] ...
