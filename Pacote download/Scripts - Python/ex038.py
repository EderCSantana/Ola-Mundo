num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior')
    print('O segundo valor é menor')
elif num2 > num1:
    print('O primeiro valor é menor')
    print('O segundo valor é maior')
elif num1 == num2:
    print('Os valores são iguais')
else:
    print('Por favor, escreva números válidos')