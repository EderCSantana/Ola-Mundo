import random
a1=str(input('Escreva o nome de um aluno: '))
a2=str(input('Escreva o nome de outro aluno: '))
a3=str(input('Escreva o nome de outro aluno: '))
a4=str(input('Escreva o nome de outro aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)
