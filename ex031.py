#Calculando o valor de uma viagem com base na distância

km = float(input('Digite quantos quilômetros terá a viagem:'))
if km <= 200:
    print('A passagem irá custar R${:.2f}' .format(km * 0.50))
else:
    print('A passagem irá custar R${:.2f}' .format(km * 0.45))
