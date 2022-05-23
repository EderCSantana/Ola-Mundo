salario = float(input('Escreva seu salário'))
if salario <= 1250:
    salario += salario*0.15
else:
    salario += salario*0.1
print('Seu salário atual é R${:.2f}'.format(salario))