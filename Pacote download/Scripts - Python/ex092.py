from datetime import datetime
ano_atual = datetime.now().year
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
dados['idade'] = ano_atual - int(input('Digite o ano de nascimento: '))
dados['carteira'] = int(input('Digite a carteira de trabalho: '))
if dados['carteira'] != 0:
    dados['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input(f'Digite o salario: '))
    dados['aposentadoria'] = ((dados['ano_contratacao']+35) - datetime.now().year)
    print(dados)
for i, j in dados.items():
    print(f'{i} tem o valor {j}')

