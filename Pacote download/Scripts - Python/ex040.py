p1 = float(input('Digite a primeira nota'))
p2 = float(input('Digite a segunda nota'))
media = (p1 + p2) / 2
if media < 5:
    print('O aluno foi reprovado')
elif media >= 5 and media <= 6.9:
    print('O aluno está de recuperação')
else:
    print('O aluno foi provado!')