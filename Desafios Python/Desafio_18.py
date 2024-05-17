import math
print('===== DESAFIO 18 =====')
angulo = int(input('Digite o valor do ângulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)

print('Para o ângulo {}, seu Seno é {:.2f} e seu Cosseno é {:.2f}'.format(angulo, seno, cosseno))