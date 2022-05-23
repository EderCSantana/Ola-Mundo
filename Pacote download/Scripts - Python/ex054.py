from datetime import date
ano = date.today().year
menor = 0
maior = 0
for i in range(0, 7):
    nascimentos = int(input('Em que ano você nasceu'))
    if ano - nascimentos< 18:
        menor += 1
    else:
        maior += 1
print('A lista tem {} menores de idade e {} maiores'.format(menor, maior))