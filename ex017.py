#utilizando biblioteca math para conseguir a hipotenusa

from math import hypot

n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(n1, n2)
'''
Utilizando o conceito matemático:
hipotenusa = (n1 ** 2 + n2 ** 2) ** (1/2)
'''

#utilizando biblioteca:

print('A hipotenusa mede: {}'.format(hi))
