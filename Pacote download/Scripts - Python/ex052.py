num = int(input('Digite um númro inteiro'))
primaridade = 1
for i in range(2, num):
    if num % i == 0:
        primaridade = 0
if primaridade == 0:
    print('Não é primo')
else:
    print('É primo')