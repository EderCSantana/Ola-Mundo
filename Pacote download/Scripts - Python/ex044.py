normal = float(input('Digite o preço normal'))
condicao = int(input('Digite o tipo de pagamento'))
if condicao == 1:
    total = normal*0.9
    print('O custo é {}'.format(total))
elif condicao == 2:
    total = normal*0.95
    print('O custo é {}'.format(total))
elif condicao == 3:
    print('O custo é {}'.format(normal))
else:
    total = normal*1.2
    print('O custo é {}'.format(total))