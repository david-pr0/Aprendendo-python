#calculando aumento de 15% de salário

valor = float(input('Digite seu salário: '))
aumento = valor*(15/100)
print('Seu novo salário com 15% de aumento será: R${:.2f}'.format(valor+aumento))
