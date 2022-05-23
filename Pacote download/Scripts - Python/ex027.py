nome = str(input('Digite seu nome completo: '))
t = nome.split()
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(t[len(t)-1]))