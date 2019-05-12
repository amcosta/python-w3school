l = []
i = 1
while i <= 5:
    n = int(input('Número {:d}: '.format(i)))
    l.append(n)
    i += 1

print(l[::-1])