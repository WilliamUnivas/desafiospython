print('===== DESAFIO 22 =====')
nome = input(str('Digite seu nome completo: ')).strip()

print('Maiúsculo: {}'.format(nome.upper()))

print('Minúsculo: {}'.format(nome.lower()))

print('Contagem de letras do nome: {}'.format(len(nome) - nome.count(' ')))

print('Contagem da primeiro nome: {}'.format(nome.find(' ')))