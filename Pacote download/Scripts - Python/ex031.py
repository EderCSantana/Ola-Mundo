vel = float(input('Escreva a velocidade '))
if vel < 200:
    print('O custo da sua viagem é R${:2}'.format(vel*0.5))
else:
    print('O custo da sua viagem é R${:2}'.format(vel*0.45))