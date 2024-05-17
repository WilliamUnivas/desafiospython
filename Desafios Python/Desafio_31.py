print('===== DESAFIO 31 =====')
numkm = int(input('Digite a distancia da viagem em Km: '))

if(numkm <= 200):
    valor = numkm * 0.5
    print('O valor da viagem é de R${:.2f}.'.format(valor))
else:
    valor = numkm * 0.45
    print('O valor da viagem é de R${:.2f}.'.format(valor))