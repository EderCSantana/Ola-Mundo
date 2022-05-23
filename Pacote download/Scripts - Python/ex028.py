import random

numPen = random.randint(0, 5)
numEsc = int(input('Em que numero eu pensei?'))
if numEsc <0 | numEsc>5:
    print('Por vavor, entre com um numero inteiro de 0 a 5')
else:
    if numPen == numEsc:
         print('Eu pensei em {}. Você acertou'.format(numPen))
    else: print('Eu pensei em {}. Você errou'.format(numPen))