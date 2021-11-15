#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

print('='* 25)
print('sequencia de fibonacci')
print('='* 25)
termos = int(input('quantos termos voce quer mostrar? '))
termo = []
n = 0
inicio = 0
inicio1 = 1
print(inicio,end=' ')
print(inicio1,end=' ')
print(inicio1,end=' ')
while len(termo) < termos + 3 :
  inicio = inicio + inicio1
  inicio1 = inicio + inicio1
  termo.append(inicio)
  termo.append(inicio1)
  n +=1
  print(termo[n],end=' ')
print('FIM')