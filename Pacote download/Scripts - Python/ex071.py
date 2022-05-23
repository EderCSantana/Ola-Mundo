valor = int(input('Quanto você gostaria de sacar?'))
nota = 50
total = valor
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        else:
            nota = 1
        totalnota = 0
        if total == 0:
            break
