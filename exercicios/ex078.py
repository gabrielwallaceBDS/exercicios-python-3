#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista = []
while len(lista) < 5:
  n = int(input('digite um valor: '))
  lista.append(n)
maior = max(lista)
menor = min(lista)
posmaior = lista.index(maior)+1
posmenor = lista.index(menor)+1
print(f'o menor valor foi {menor} e apareceu na posicao {posmenor}')
print(f'o maior valor foi {maior} e apareceu na posiçao {posmaior}')
print(lista)