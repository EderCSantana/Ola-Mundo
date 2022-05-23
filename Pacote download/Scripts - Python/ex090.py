alunos = dict()
lista = list()
while True:
    alunos['nome'] = str(input('Digite o nome do aluno: '))
    alunos['média'] = float(input('Digite média do aluno: '))
    if alunos['média'] < 3:
        alunos['stituação'] = 'reprovado'
    elif alunos['média'] < 5:
        alunos['stituação'] = 'recuperação'
    else:
        alunos['situação'] = 'aprovado'
    lista.append(alunos.copy().values())
    alunos.clear()
    continuar = str(input('Gostaria de continuar? [s/n]')).strip().lower()
    if continuar in 'nN':
        break
print(lista)