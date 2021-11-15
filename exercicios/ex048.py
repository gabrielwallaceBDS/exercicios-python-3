#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range (1,500):
  if i % 3 == 0 and i % 2 == 1:
    soma +=1
    print(i)
print(soma)
