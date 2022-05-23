num = int(input('Digite um número: '))
print('A tabuada desse número é ')
for i in range(0, 11):
    print('{} x {} = {}'.format(num, i, num*i))