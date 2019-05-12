arquivo = open('numeros.txt', 'w')
linha = 1
for linha in range(20):
    arquivo.write('{:d}\n'.format(linha))
arquivo.close()