num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: '))
       )
noves = 0
cont = 0
for i in num:
    print(f'{i}', end='')
print('')
for i in num:
    cont += 1
    if i%2 == 0:
        print(f'{i} é par')
    if i == 9:
        noves += 1
    if i == 3:
        print(f'A posição {cont} contem um 3')
print(f'Você digitou {noves} vez(es) o número 9')
