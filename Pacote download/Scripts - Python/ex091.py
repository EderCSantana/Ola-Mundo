from random import randint
from operator import itemgetter
jogador = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
lista = list()
print(jogador)
for i, j in jogador.items():
    print(f'{i} tirou {j}')
lista = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(lista):
    print(f'O {i+1}º lugar: {j[0]} tirou {j[1]}')
