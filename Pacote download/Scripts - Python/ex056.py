media = 0
max = 0
maisvelho = ''
numeromulheres = 0
for i in range(0, 4):
    nome = str(input('Digite seu nome '))
    idade = int(input('Digite sua idade '))
    sexo = str(input('Digite o seu sexo '))
    media += idade
    if sexo == 'm' and i == 0:
        if max < idade:
            max = idade
            maisvelho = nome
    if sexo == 'f' and idade < 20:
        numeromulheres += 1
media /= 4
print('A média de idade no grupo é {}'.format(media))
if maisvelho != '':
    print('O homem mais velho é {}'.format(maisvelho))
if numeromulheres > 0:
    print('O grupo tem {} mulheres com menos de 20 anos'.format(numeromulheres))
