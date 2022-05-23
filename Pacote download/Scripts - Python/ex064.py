n = int(input('Digite [999] para parar '))
soma = 0
cont =0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite [999] para parar '))
print(' Você digitou {} números e a soma deles é {}'.format(cont, soma))