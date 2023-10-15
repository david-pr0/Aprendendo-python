#análisando string
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas: {}' .format(nome.upper()))
print('Seu nome em letras minúsculas: {}' .format(nome.lower()))
print('Seu nome contém {} letras.' .format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.' .format(nome.find(' ')))

'''Forma alternativa para exibir o primeiro nome e contar suas letras
nome = nome.split()
print('Seu primeiro nome é {} e tem {} letras.' .format(nome[0], len(nome[0])))'''

'''Outra forma alternativa para a mesma função
n1 = nome.find(' ')
print('Seu primeiro nome é {} e tem {} letras.' .format(nome[:n1], nome.find(' ')))'''
