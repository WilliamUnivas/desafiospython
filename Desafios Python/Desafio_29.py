print('===== DESAFIO 29 =====')
velocidade = int(input('Qual a velocidade o carro passou do radar? '))

if(velocidade > 80):
    multa = (velocidade - 80) * 7
    print('Você ultrapassou a velocidade permitida e deve pagar o valor de R${:.2f}.'.format(multa))
else:
    print('O carro passou dentro da velocidade permitida')