print('===== DESAFIO 34 =====')
salario = int(input('Digite seu salário: '))

if(salario > 1250):
    aumento = salario * 1.1
    print('O seu salário agora é R${:.2f}.'.format(aumento))
else:
    aumento = salario * 1.15
    print('O seu salário agora é R${:.2f}.'.format(aumento))