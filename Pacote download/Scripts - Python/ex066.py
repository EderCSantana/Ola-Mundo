soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Você digitou {cont} números e a soma deles é {soma}')