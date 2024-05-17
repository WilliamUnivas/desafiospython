import math
print('===== DESAFIO 17 =====')
catoposto = int(input("Qual o valor do cateto oposto? "))
catadjacente = int(input("Qual o valor do cateto adjacente? "))
hipotenusa = math.sqrt(math.pow(catadjacente, 2) + math.pow(catoposto, 2))

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))