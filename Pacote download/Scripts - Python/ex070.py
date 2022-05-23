soma = carinho = cont = menor = 0
while True:
    nome = str(input('Digite o nome do produto '))
    valor = float(input('Digite o preço do produto '))
    soma += valor
    cont += 1
    if valor > 1000:
        carinho += 1
    if cont == 1 or menor > valor:
        menor = valor
        baratoso = nome
    continuar = input('Você quer continuar? [s/n]').strip().upper()[0]
    if continuar in 'N':
        break
print(f'''
    O gasto total da compra foi R${soma:.2f}
    Você comprou {carinho} produtos acma de R$1000,00
    O produto mais barato foi {baratoso} que custa {menor:.2f}
''')
