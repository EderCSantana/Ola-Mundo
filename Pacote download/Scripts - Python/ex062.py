atual = int(input('Digite o primeiro termo da nossa PA: '))
razao = int(input('Digite a razao da nossa PA: '))
i = 0
while i < 10:
    print('{} -> '.format(atual), end='')
    atual += razao
    i += 1
print('')
i = 0
j = int(input('Gostaria de mais tentativas? Digite quantas mais você quer'))
if j != 0:
    while i < j:
        print('{} -> '.format(atual), end='')
        atual += razao
        i += 1
    print('')
    j = int(input('Gostaria de mais tentativas? Digite quantas mais você quer'))
else:
    print('FIM')
