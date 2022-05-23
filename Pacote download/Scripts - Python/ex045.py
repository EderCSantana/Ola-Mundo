from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
num = int(input('''Digite um numero:
0 - pedra
1 - papel
2 - teoura
'''))
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[num]))
if (num == 0 and computador == 2) or (num == 1 and computador ==0) or (num == 2 and computador == 1):
    print('Parabéns, você ganhou!')
elif (num == 2 and computador == 0) or (num == 0 and computador ==1) or (num == 1 and computador == 2):
    print('O computador ganhou!')
else:
    print('Empate!')