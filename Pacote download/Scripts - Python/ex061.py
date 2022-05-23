primeiro = int(input('Digite o primeiro termo da nossa PA '))
razao = int(input('Digite a razao da nossa PA '))
i = 0
while i < 10:
    print('{} -> '.format(primeiro+(razao*i)), end='')
    i += 1
