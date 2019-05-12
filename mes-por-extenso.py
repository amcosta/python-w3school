meses = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro'
]

texto = input('Digite a data do seu nascimento (dd/mm/aaaa): ')
partes = texto.split('/')

mes = meses[int(partes[1]) - 1]

print('Você nasceu no dia {:s} de {:s} de {:s}'.format(partes[0], mes, partes[2]))