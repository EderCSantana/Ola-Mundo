caracteristicas = []
pessoas = []
cont = 0
maior = menor = 0
pesado = []
leve = []
while True:
    caracteristicas.append(str(input('Digite o nome: ')))
    caracteristicas.append(float(input('Digite o peso: ')))
    pessoas.append(caracteristicas[:])
    caracteristicas.clear()
    if cont == 0:
        maior = pessoas[0][1]
        menor = pessoas[0][1]
    else:
        if maior < pessoas[cont][1]:
            maior = pessoas[cont][1]
        if menor > pessoas[cont][1]:
            menor = pessoas[cont][1]
    cont += 1
    continuar = str(input('Deseja continuar? [s/n]')).strip().lower()
    if continuar in 'n':
        break
for i in range(0, cont):
    if maior == pessoas[i][1]:
        pesado.append(pessoas[i][0])
    if menor == pessoas[i][1]:
        leve.append(pessoas[i][0])

print(pessoas)
print(f'{cont} pessoas se cadastraram')
print(f'As pessoas mais leves são {leve} que pesam {menor} ')
print(f'As pessoas mais pesadas são {pesado} que pesam {maior} ')
