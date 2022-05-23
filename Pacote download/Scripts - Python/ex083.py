parangole = []
equa = str(input('Digite um número '))
for i in equa:
    if i == '(':
        parangole.append('(')
    elif i == ')':
        if len(parangole) > 0:
            parangole.pop()
        else:
            parangole.append(')')
            break
if len(parangole) == 0:
    print('Tudo certo!')
else:
    print('Ta errado!')