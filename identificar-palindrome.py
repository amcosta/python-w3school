texto = input('Digite a palavra: ')
resultado = 'é' if texto[::-1] == texto else 'não é'
print('A palavra {:s} {:s} palíndrome'.format(texto, resultado))