#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continuar = 'S'
num = maior = menor = soma = vezes = 0
while continuar not in 'N':
  num = int(input('digite um numero: '))
  continuar = str(input('quer continuar? [S/N]')).upper()
  soma = soma + num 
  vezes +=1
  if maior < num:
    maior = num
  if num < maior:
    menor = num
print('''voce digitou {} numeros e a media entre eles foi {}
o maior valor é de {} e o menor é {}'''.format(vezes, soma/vezes,maior, menor  ))

  
