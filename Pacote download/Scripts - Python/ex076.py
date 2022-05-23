listagem = ('Batata', 2.50,
            'Mrkev', 1.23,
            'Chuchu', 3.40)
print('-'*40)
print(f'{"Listagem de preços":40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
