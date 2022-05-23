soma = cont = 0
num = int(input('Digite um número '))
resposta = str(input('Deseja continuar? [s/n]'))
menor = maior = num
while resposta in 'Ss':
    num = int(input('Digite um número '))
    resposta = str(input('Deseja continuar? [s/n]'))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma/cont
print('Você escreveu {} números. '.format(cont))
print('O maior é {}, o menor é {} e a media deles é {}.'.format(maior, menor, media))
