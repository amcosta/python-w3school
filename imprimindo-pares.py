limite = int(input('Digite um número: '))

posicao = 1
while posicao <= limite:
    if posicao % 2 == 0:
        print('Número: {:d}'.format(posicao))
    posicao += 1