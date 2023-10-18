#jogo de adivinhação

from random import randint
from time import sleep

n = randint(0, 5)
n2 = int(input('Pensei em um número, tente adivinhar qual: '))
print('Processando...')
sleep(3)
if n2 == n:
    print('Parabéns você acertou!')
else:
    print('Que pena, pensei no número {}, tente novamente.' .format(n))
