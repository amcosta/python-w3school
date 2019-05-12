def fatorial(numero, quantidade):
    fat = 1
    i = 1

    for i in range(quantidade):
        fat *= numero

    return fat


numero, quantidade = input('Diginte o número e a quantidade (separado por virgula): ').split(',')
print(fatorial(int(numero), int(quantidade)))