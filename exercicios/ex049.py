#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('digite um numero para ver sua tabuada'))
for i in range(0,11):
  vezes = num * i
  print('{} x {} = {}'.format(num, i, vezes))