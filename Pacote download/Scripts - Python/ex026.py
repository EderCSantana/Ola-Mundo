frase = str(input('Digite uma frase'))
print('A letra "A" aparece {} vezes'.format(frase.lower().count('a')))
print('A primeira aparição de "A" é na posição {}'.format(frase.find('a')+1))
print('A última aparição de "A" é na posição {}'.format(frase.rfind('a')+1))