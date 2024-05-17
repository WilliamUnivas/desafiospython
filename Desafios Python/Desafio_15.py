print('===== DESAFIO 15 =====')
quantdias = int(input('Por quantos dias o carro foi alugado? '))
kmrodados = float(input('Quanto Km o carro rodou? '))

print('O valor total a pagar é de R${:.2f}.'.format(quantdias * 60 + kmrodados * 0.15))