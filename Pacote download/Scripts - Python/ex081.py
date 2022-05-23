lista = []
while True:
    lista.append(int(input('Digite um número ')))
    continuar = str(input('Quer continuar? [s/n]')).lower()
    if continuar in 'n':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} números')
print(f'Sua lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na sua lista')
else:
    print('O número 5 não está na sua lista')

