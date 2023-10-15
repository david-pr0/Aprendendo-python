#Mostrando primeiro e ultimo nome de uma string

nome = input('Digite seu nome completo: ').strip().split()
print('Seu primeiro nome é: {}' .format(nome[0]))
print('Seu ultimo nome é: {}' .format(nome[len(nome) - 1]))
