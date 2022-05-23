matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira = segunda = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o elemento [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            par += matriz[i][j]
        if j == 2:
            terceira += matriz[i][j]
for i in range(0, 3):
    if i == 0:
        segunda = matriz[1][i]
    elif segunda < matriz[1][i]:
        segunda = matriz[1][i]

print(f'''
    A matriz digitada foi:
    {matriz[0][:]}
    {matriz[1][:]}
    {matriz[2][:]}
    A soma dos valores pares é {par}
    A soma dos valores da terceira coluna são {terceira}
    O maior valor da segunda linha é {segunda}
    
''')
