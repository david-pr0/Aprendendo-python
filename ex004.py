#análise de uma variável

a=input("Digite algo: ")
print('O tipo primitivo é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É alfa numérico? ', a.isalnum())
print('Só tem algarismos? ', a.isalpha())
print('Está maiusculo? ', a.isupper())
print('Está minúsculo? ', a.islower())
print('É decimal? ', a.isdecimal())
print('É um número? ', a.isnumeric())
