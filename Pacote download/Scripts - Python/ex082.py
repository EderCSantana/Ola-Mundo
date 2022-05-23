lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número '))
    lista.append(num)
    contunuar = str(input('Deseja continuar? [s/n] ')).lower()
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
    if contunuar in 'n':
        break
print(f'''
    A lista original é {lista}
    A lista de pares é {par}
    A lista de ímpares é {impar}
''')