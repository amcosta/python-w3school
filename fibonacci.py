limite = int(input('Digite o limite: '))
a, b = 1, 1
i = 3
while i <= limite:
    a, b = b, a + b
    i += 1

print('O resultado é: {:d}'.format(b))