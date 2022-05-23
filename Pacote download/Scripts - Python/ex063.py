n = int(input('Digite o número de termos que você quer na sua sequência de Fibonacci: '))
efeDeN = 0
efeDeNMaisUm = 1
if n > 0:
    print('{}'.format(efeDeN), end='')
    n -= 1
    if n > 0:
        print(' - {}'.format(efeDeNMaisUm), end='')
        n -= 1
    while n > 0:
        efeDeNMaisDois = efeDeN + efeDeNMaisUm
        print(' - {}'.format(efeDeNMaisDois), end='')
        efeDeN = efeDeNMaisUm
        efeDeNMaisUm = efeDeNMaisDois
        n -= 1
