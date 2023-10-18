#lendo velocidade de um carro e decidindo se ele está acima do limite de velocidade

velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade <= 80:
    print('Tenha uma boa viagem!')
else:
    print('Você terá que pagar uma multa de R${:.2f}' .format((velocidade - 80) * 7))
