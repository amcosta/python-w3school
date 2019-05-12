precoLata = 80
litrosLata = 18
metrosPorLitro = 3

metrosPorLata = litrosLata * metrosPorLitro

area = int(input('Informe o valor da área pintada: '))

quantidadeLatas = int(area / metrosPorLata)

if area % metrosPorLata != 0:
    quantidadeLatas += 1

print('Para pintar a área de {:d}m² são necessárias {:d} latas, com o total de R$ {:.2f}'.format(area, quantidadeLatas, quantidadeLatas * precoLata))