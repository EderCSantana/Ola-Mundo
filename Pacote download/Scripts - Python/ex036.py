valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digire o salario: '))
anos = float(input('Digite a quantidade de anos: '))
prestacao = valorCasa  / (salario*12)
minimo = salario*0.3
print('Com o valor da casa de {:.2f} e um salário de {:.2f}'.format(valorCasa, salario), end=' ')
print('A prestação é de {:.2f} e o mínimo para ser aceito é {:.2f}'.format(prestacao,minimo))
if prestacao <= minimo:
    print('Empréstimo aprovado!')
else: print('Emprestimo negado.')