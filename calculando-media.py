limite = 5
x = 1
soma = 0

while x <= limite:
    numero = int(input('Digite o número {:d}: '.format(x)))
    soma += numero
    x += 1

print('A média é {:.2f}'.format(soma / limite))