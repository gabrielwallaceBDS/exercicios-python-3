#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('digite um numero: '))
res = num % 2
if res == 1:
  print('numero impar')
else:
  print('numero par')
