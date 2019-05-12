numero = int(input('Digite o número: '))
limite = int(input('Digite o limite: '))

posicao = 1
fatorial = numero
while posicao <= limite:
    fatorial *= numero
    posicao += 1
print('O fatorial é {:d}'.format(fatorial))