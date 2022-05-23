jogador = dict()
gols = list()
soma = 0
val = 0
jogador['nome'] = str(input('Digite o nome de um jogador: '))
jogador['partidas'] = int(input(f'Digite o número de partidas do(a) {jogador["nome"]}: '))

for i in range(0, jogador['partidas']):
    val = int(input(f'O número de gols na {i+1} partida foi: '))
    gols.append(val)
    soma += val
jogador['num_gols'] = gols
jogador['total_gols'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for i, j in jogador.items():
    print(f'O campo {i} tem valor {j}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["num_gols"])}')
for i, j in enumerate(jogador['num_gols']):
    print(f'Na patida {i} ele fez {j}')
print(f'Foi um total de {jogador["total_gols"]}')
