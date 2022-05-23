from random import randint
num = int(input('Quanros jogos você quer jogar?'))
jogos = []
lista = []
total = 1
while total <= num:
    cont = 0
    while True:
        alea = randint(1, 60)
        if alea not in lista:
            lista.append(alea)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(jogos)
