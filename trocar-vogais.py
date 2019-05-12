texto = input('Digite o texto: ')

saida = []
i = 0

while i < len(texto):
    saida.append('*' if texto[i] in 'aeiou' else texto[i])
    i += 1

print(''.join(saida))