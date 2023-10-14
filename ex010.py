#conversão de reais em dolar

n1 = float(input('Quantos reais você tem? '))
n2 = float(input('Quanto está valendo o dolar hoje? '))
print('Com essa quantidade você consegue comprar US${:.2f} dolares.'.format(n1/n2))
