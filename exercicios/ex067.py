#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
num = 1
while num > 0:
  print('-' * 30)
  num = int(input('digite um numero para ver sua tabuada: '))
  if num < 0:
    break
  else:
    print('-' * 30)
    for i in range(0,11):
      vezes = num * i
      print(f'{num} x {i} = {vezes}')
  
print('programa de tabuada encerrado, volte sempre! ')