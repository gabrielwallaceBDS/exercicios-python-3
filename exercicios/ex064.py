#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = 0
n1 = 0
vezes = 0
while n != 999:
  n = int(input('digite u numero[999 para parar]: '))
  n1 = n1 + n
  n = n
  vezes+=1
print('voce digitou {} valores e a soma deles é de {}'.format(vezes -1,n1 - 999))
