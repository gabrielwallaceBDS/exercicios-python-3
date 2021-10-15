#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
number = int(input('digite um numero inteiro: '))
print('''escolha uma das opçoes
1 para binario
2 para octal 
3 para hexadecimal
''')
option = int(input('qual opçao desejada? '))
if option == '1' or option == 1:
  bina = bin(number)
  print('o numero {} convertido em binario é {}'.format(number,bina[2:]))
if option == '2' or option == 2:
  octa = oct(number)
  print('o numero {} convertido em octal é {}'.format(number,octa[2:]))
if option == '3' or option == 3:
  hexa = hex(number)
  print('o numero {} convertido em hexadecimal é {}'.format(number, hexa[2:]))
