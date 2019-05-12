n1 = int(input('N1: '))
n2 = int(input('N2: '))

mdc = 1
i = 1
while i <= n1 or i <= n2:
    if n1 % i == 0 and n2 % i == 0:
        mdc = i
    i += 1

print('O MDC de {:d} e {:d} é: {:d}'.format(n1, n2, mdc))