#calculando quantos litros de tinta serão usados para pintar uma parede

a = float(input('Digite quantos metros de altura tem a parede: '))
l = float(input('Digite quantos metros de largura tem a parede: '))
t = a * l
print('Você precisará de {}L de tinta para pintar toda a parede.'.format(t / 2))
