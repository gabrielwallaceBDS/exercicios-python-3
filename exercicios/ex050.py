#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
pares = []
soma = 0
for c in range(1, 7):
  num = int(input('valor {}'.format(c)))
  if num % 2 == 0:
    soma =soma + num
    pares.append(num)
print(soma)
print(pares) 