vel = float(input('Qual é a sua velocidade?'))
if vel < 80:
    print('Muito bem, dirija com segurança.')
else: print('Você está a {}km/h. Voce foi multado e terá que pagar R${:2}'.format(vel,(vel-80)*7))