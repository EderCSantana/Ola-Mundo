from random import randint
numcomp = randint(0, 10)
numUsuario = int(input('Eu pensei em um número, sabe qual? '))
tentativa = 1
while numUsuario != numcomp:
    print('errrrrouu')
    tentativa += 1
    numUsuario = int(input('Eu pensei em um número, sabe qual? '))
print('Parabéns, depois de {} tentativas você achou o número certo. '.format(tentativa))
