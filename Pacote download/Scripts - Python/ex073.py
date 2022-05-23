times = ('Flamengo', 'Internacional', 'Atlético-MG',
         'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos'
         'Atlético-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO'
         'Bahia', 'Sport Recife',  'Fortaleza', 'Vasco da Gama', 'Goiás',
         'Coritiba', 'Botafogo'
         )
print(f'Os promeiros 5 times são : {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)} ')
print(f'O Fluminense está na {times.index("Fluminense")+1} posição')
