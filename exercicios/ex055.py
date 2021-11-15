#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
for i in range (1,6):
  peso = float(input('peso da {}° pessoa: '.format(i)))
  pesos.append(peso) 
peso1 = sorted(pesos)
print(pesos)
print(peso1)
print(peso1[0])
print(peso1[4])