first = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão de nossa PA '))
for i in range(0, 10):
    first = first + razao
    print(first, end = ' ')