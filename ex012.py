#conseguindo o valor de um produto com 5% de desconto

valor = float(input('Digite o valor do produto: '))
desconto = valor*(5/100)
print('O valor do item com 5% de desconto é: R${:.2f}'.format(valor-desconto))
