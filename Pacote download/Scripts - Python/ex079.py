lista = []
while True:
    a = int(input('Digite um número '))
    if a in lista:
        print('Ja temos esse número, entre com outro')
    else:
        lista.append(a)
    continuar = str(input('Deseja continuar? [s/n] ').lower())
    if continuar in 'n':
        break
lista.sort()
print(f'Você digitou {lista}')