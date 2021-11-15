#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('digite um numero'))
n = []
for i in range (1, num + 1):
  if num % i == 0:
    print('\033[33m{}'.format(i),end = ' ')
    n.append(i)
  else:
    print('\033[31m{}'.format(i),end = ' ')
total = len(n) 
if total == 2:
  print('numero primo')
else:
  print('numero nao é primo')
