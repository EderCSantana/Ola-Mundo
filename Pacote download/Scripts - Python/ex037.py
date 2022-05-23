num = int(input('Digite um número: '))
opcao = int(input('''Escolha o tipo de conversão: 
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal'''))
if opcao == 1:
    print('{} em binário é {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} em octal é {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)))
else:
    print('Escreva um número válido')