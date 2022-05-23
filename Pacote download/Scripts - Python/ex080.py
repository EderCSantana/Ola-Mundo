lista = []
aux = 0
for i in range(0, 5):
    n = (int(input('Digite um número ')))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        j=0
        while j < len(lista):
            if n <= lista[j]:
                lista.insert(j, n)
                break
            j += 1
print(lista)
