numeros = []
pares = []
impares = []
for i in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
impares.sort()
pares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print(f'A lista de números é {numeros}')

