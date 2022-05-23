demaior = 0
numHomens = 0
numMulheres = 0
while True:
    idade = int(input('Qual é a idade dessa pesssoa? '))
    sexo = str(input('Qual é o sexo dessa pessoa? '))
    if idade > 18:
        demaior += 1
    if sexo in "Mm":
        numHomens += 1
    if sexo in "Ff" and idade < 20:
        numMulheres += 1
    continuar = str(input('Gostaria de continuar? [s/n]'))
    if continuar in "Nn":
        break
print(f'''
    Entre as pessoas escritas
    {demaior} são maiores de 18 anos
    {numHomens} são homens
    {numMulheres} são mulheres menores de 20 anos
    ''')