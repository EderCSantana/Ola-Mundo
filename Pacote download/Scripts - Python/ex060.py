num = int(input('digite um número'))
i = num
original = num
while i > 1:
    i -= 1
    num *= i
print('{}! = {}'.format(original, num))