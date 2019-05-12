texto = input('Digite o texto: ')

vogais = []
contador = 0
i = 0

while i < len(texto):
    if texto[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        contador += 1
        vogais.append(texto[i])
    i += 1

print('Encontrei {:d} vogais no texto'.format(contador), set(vogais))