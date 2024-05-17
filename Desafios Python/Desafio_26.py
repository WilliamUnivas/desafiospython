print('===== DESAFIO 26 =====')
frase = str(input('Digite uma frase: ')).strip()

print('Quantidade de vezes que a letra A aparece: {}'.format(frase.upper().count('A')))

print('Posição da primeira letra A: {}'.format(frase.upper().find('A') + 1))

print('Posição da última letra A: {}'.format(frase.upper().rfind('A') + 1))