import random
print('===== DESAFIO 28 =====')
numusuario = int(input('Digite um número de 1 até 5: '))
numsistema = random.randint(1, 5)

if(numusuario == numsistema):
    print('Parabéns, o número {} era o correto, VOCÊ VENCEU!!!'.format(numsistema))
else:
    print('Você perdeu! O número correto era o {}'.format(numsistema))