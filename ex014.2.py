#convertendo °F em °C

temp = float(input('Informe a temperatura em °F: '))
conv = (temp - 32) / 1.8
print('A temperatura informada corresponde a :{:.1f}°C'.format(conv))
