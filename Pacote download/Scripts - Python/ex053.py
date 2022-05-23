frase = input('Digite uma frase ').strip().upper()
separado = frase.split()
junto = ''.join(separado)
print(junto)
tamanho = len(junto)
épalindromo = 0
for i in range(0, tamanho):
    if junto[i] == junto[tamanho - 1 -i]:
        épalindromo += 1
        print(junto[i])
print(épalindromo)
if épalindromo == tamanho:
    print('É um palindromo')
else:
    print('Não é um palíndromo')
