numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'desenove', 'vinte')
num = int(input('Digite um número '))
if num < 0 or num > 20:
    print('Digite um número adequado, cabaço...')
else:
    a = numeros[num]
    print(f'Você digitou o número {a}')
