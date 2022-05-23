sexo = input('Digite seu sexo com M para homem e F para mulher:  ')
while sexo != "M" and sexo != "F":
    print('Valores inválidos. Por favor, escreva um o sexo corretamente')
    sexo = input('Digite seu sexo com M para homem e F para mulher')
print('Seu sexo é {}'.format(sexo))
#também é possível com:
#while sexo not in 'MmFf':