#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))
menor = n1
#verificando menor
if n2 < n1 and n2 < n3:
  menor = n2
if n3 < n1 and n3 < n2:
  menor = n3
#verificando maior
maior = n1
if n2 > n1 and n2 > n3:
  maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
print('maior {}\nmenor {}'.format(maior,menor))



'''
if n1 > n2 and n1 > n3:
  print('{} é o maior numero'.format(n1))
if n2 > n1 and n2 > n3:
  print('{} é o maior numero'.format(n2))
if n3 > n1 and n3 > n1:
  print('{} é o maior numero'.format(n3))
#menor
if n1 < n2 and n1 < n3:
  print('{} é o menor numero'.format(n1))
if n2 < n1 and n2 < n3:
  print('{} é o menor numero'.format(n2))
if n3 < n1 and n3 < n2:
  print('{} é o menor numero'.format(n3))'''
  