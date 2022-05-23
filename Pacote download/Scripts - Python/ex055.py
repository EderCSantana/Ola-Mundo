min = 0
max = 0
for i in range(0, 5):
    peso = float(input('Digite seu peso'))
    if i == 0:
        min = peso
        max = peso
    if peso < min:
        min = peso
    if peso > max:
        max = peso
print('O mínimo é {} e o máximo é {}'.format(min, max))