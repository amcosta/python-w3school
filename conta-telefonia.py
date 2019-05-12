empresa = 'Tchau'

minutos = int(input('Informe a quantidade de minutos da conta: '))

preco = 0.15

if minutos < 200:
    preco = 0.2

if minutos >= 200 and minutos <= 400:
    preco = 0.18

if minutos > 800:
    preco = 0.8

print('O valor da sua conta é: R$ {:.2f}'.format(minutos * preco))