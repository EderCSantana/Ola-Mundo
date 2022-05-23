sair = 0
while sair != 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print('Qual atividade gostaria de fazer?')
    sair = int(input('''
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa'''))
    if sair == 1:
        print('A soma dos valores é {}.'.format(num1+num2))
    elif sair == 2:
        print('O produto dos valores é {}.'.format(num1*num2))
    elif sair == 3:
        if num1 > num2:
            print('O maior é: {}.'.format(num1))
        elif num2 > num1:
            print('O maior é: {}.'.format(num2))
        else:
            print('Ninguém é maior, os números são iguais.')
    else:
        print('Por favor, use valores possíveis.')
        sair = int(input('''[1] somar
                     [2] multiplicar
                     [3] maior
                     [4] novos números
                     [5] sair do programa'''))
