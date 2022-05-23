import math
from datetime import date
atual = date.today().year
nasc = int(input('Digite sua data de nascimento'))
alist = abs(atual - nasc)
print(alist)
if alist >0 and alist < 18:
    print('Você vai se alistar daqui {}'.format(18 - alist))
elif alist > 18:
    print('Você devia ter se alistado faz {}'.format(alist - 18))
else:
    print('Fica esperto, você vai alistar esse ano')