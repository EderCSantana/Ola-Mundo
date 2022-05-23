matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o elemento [{i}][{j}]: '))
print(f'''
    A matriz digitada foi:
    {matriz[0][:]}
    {matriz[1][:]}
    {matriz[2][:]}
''')
