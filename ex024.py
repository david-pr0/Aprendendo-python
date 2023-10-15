#Conferindo se uma frase inicia em uma certa palavra

nome = input('Digite a cidade que você nasceu: ')
nome = nome.upper()
nome = nome.split()
print('SANTO' in nome[0])

#Resolução alternativa
'''nome = input('Digite a cidade que você nasceu: ').strip()
print(nome[:5].upper() == 'SANTO')'''
