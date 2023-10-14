#calculando o aluguel de um veículo com base em tempo e km utilizados

km = float(input('Quantos km você percorreu? '))
dia = int(input('Por quantos dias você alugou o carro? '))
valor = (dia * 60) + (km * 0.15)
print('O valor total a ser pago é: R${:.2f}'.format(valor))
