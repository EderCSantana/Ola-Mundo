from random import randint
cont = 0
while True:
    escolha = str(input('Par ou ímpar?'))
    num = int(input())
    compnum = randint(0, 11)
    paridade = (num + compnum)%2
    if paridade == 0:
        epar = True
    else:
        epar = False
    if escolha in 'Pp' and epar == True or escolha in 'Ii' and epar == False:
        cont += 1
        print(f'{compnum} e {num}, você venceu.')
    else:
        break
print(f'{compnum} e {num} você perdeu e venceu {cont} vezes.')