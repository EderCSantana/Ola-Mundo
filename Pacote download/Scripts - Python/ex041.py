from datetime import date
nascimento = int(input('Digite o ano de seu nascimento'))
idade = date.today().year - nascimento
if idade > 0 and idade < 9:
    print('Você é da categoria MIRIM')
elif idade >= 9 and idade < 14:
    print('Você é da categoria INFANTIL')
elif idade >=14 and idade < 19:
    print('Você é da categoria JUNIOR')
elif idade >= 19 and idade < 25:
    print('Você é da categoria SÊNIOR')
else:
    print('Você é da categoria MASTER')