#Primeira e ultima ocorrência de uma string

nome = input('Digite seu nome completo: ').upper().strip()
print('Analisando...')
print('A letra (A) aparece {} vezes em seu nome.' .format(nome.upper().count('A')))
print('A letra (A) aparece pela primeira vez na {}° posição.' .format(nome.find('A') + 1))
print('A letra (A) aparece pela ultima vez na {}° posição.' .format(nome.rfind('A') + 1))
