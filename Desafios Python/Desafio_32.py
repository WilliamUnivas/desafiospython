print('===== DESAFIO 32 =====')
ano = int(input('Digite um ano qualquer: '))

if(ano % 4 == 0):
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))