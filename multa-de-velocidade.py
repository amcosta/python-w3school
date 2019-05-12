limiteDeVelocidade = 100
multaPorKm = 5

velocidade = int(input('Informe a valicidade do veiculo'))

if velocidade > limiteDeVelocidade:
    print('O veiculo esta acima da velocidade permitida');
    multa = (velocidade - limiteDeVelocidade) * multaPorKm
    print('O valor da multa é: R$ {:.2f}'.format(multa))
else:
    print('O veiculo esta dentro da velocidade permitida')