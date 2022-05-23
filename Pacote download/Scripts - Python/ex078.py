cont = 0
listinha = []
for i in range(0, 5):
    listinha.append(int(input('Digite um número ')))
print(f'Sua lista é {listinha}')
print(f'O maior valor é {max(listinha)} e o menor é {min(listinha)}')
print(f'Suas posições são {listinha.index(max(listinha))+1} e '
      f'{listinha.index(min(listinha))+1}, respectivamente.')
