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
dia, mes, ano = texto.split('/')
print('Você nasceu no dia {:s} de {:s} de {:s}'.format(dia, meses[int(mes) - 1], ano))