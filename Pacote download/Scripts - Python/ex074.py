from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
for i in num:
    print(i, end=' ')
print(f'O menor númro é {min(num)} e o maior é {max(num)}')
