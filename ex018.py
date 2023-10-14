#utilizando biblioteca math para conseguir a tangente

from math import sin, cos, tan, radians
a = float(input('Digite o ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O seno de {} é: {:.2f} \nO cosseno de {} é: {:.2f} \nA tangente de {} é: {:.2f}'.format(a, sen, a, cos, a, tan))
