soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        soma += i
print(soma)