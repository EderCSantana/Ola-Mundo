alunos = []
lista = []
nomes = []
notas = []
cont = 0
while True:
    nomes.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota da P1: ')))
    notas.append(float(input('Nota da P2: ')))
    media = (notas[0] + notas[1])/2
    alunos.append(nomes[:])
    alunos.append(notas[:])
    alunos.append(media)
    nomes.clear()
    notas.clear()
    lista.append(alunos[:])
    alunos.clear()
    contunuar = str(input('Quer continuar? [s/n] ')).strip().lower()
    cont += 1
    if contunuar in 'n':
        break
for i, a in enumerate(lista):
    print(f'{i}   {a[0]}   {a[2]}')
while True:
    olhar = int(input('Gostaria de ver as notas de alguém? '))
    if olhar == 999:
        break
    else:
        print(f'{lista[olhar][0]}  {lista[olhar][1]}')
