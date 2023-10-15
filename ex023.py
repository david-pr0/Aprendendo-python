#separando números através de lógica matemática

n = int(input('Digite um número de 0 à 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Milhar: {} \nCentena: {} \nDezena: {} \nUnidade: {}' .format(m, c, d, u))
