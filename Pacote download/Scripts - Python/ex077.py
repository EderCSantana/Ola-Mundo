palavras = ('brambora', 'mleko', 'banan', 'jablko')
for i in palavras:
    print(f'Na palavra {i} temos: ', end='')
    for j in i:
        if j in 'aeiou':
            print(j, end='')
    print('')
