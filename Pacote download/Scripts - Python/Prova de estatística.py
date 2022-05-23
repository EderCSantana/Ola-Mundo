from math import sqrt
escolha = str(input('''
            Qual variavel você procura? 
            d para delta
            n para n
            t para confidencia 
'''))
t = 0
s2 = 0
n = 0
erro = 0
delta = 0
if escolha in 'dD':

    t = float(input('T ou U = '))
    s2 = float(input('S^2 = '))
    n = float(input('n = '))
    erro = sqrt(s2 / n)
    delta = t * erro
    print(f'Delta = {delta}')
elif escolha in 'nN':
    t = float(input('T ou U = '))
    s2 = float(input('S^2 = '))
    delta = float(input('delta = '))
    n = ((t*t) * s2)/(delta*delta)
    print(f'n = {n}')
elif escolha in 't':
    s2 = float(input('S^2 = '))
    delta = float(input('delta = '))
    n = float(input('n = '))
    t = delta * sqrt(n/s2)
    print(f'T = {t}')
