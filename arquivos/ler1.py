arquivo = open('numeros.txt')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()