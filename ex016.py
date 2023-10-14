'''
usando função trunc para retornar porção inteira
from math import trunc

num = float(input('Digite um número real: '))
porc = trunc(num)
print('O número digitado é: {} e sua porção inteira é: {}.'.format(num,porc))'''

#usando funções internas para retornar porção inteira
num = float(input('Digite um número real: '))
print('O valor informado é: {} e sua porção inteira é: {}.'.format(num, int(num)))
