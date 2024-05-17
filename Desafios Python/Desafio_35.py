print('===== DESAFIO 35 =====')
l1 = int(input('Digite o cumprimento da primeira reta: '))
l2 = int(input('Digite o cumprimento da segunda reta: '))
l3 = int(input('Digite o cumprimento da terceira reta: '))

if(l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1):
    print('Essas retas não formam um triângulo.')
else:
    print('Essas retas formam um triângulo')