#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('primeiro lado: '))
r2 = float(input('segundo lado: '))
r3 = float(input('terceiro lado: '))

if r1 + r2 < r3:
  print('nao forma um triangulo')
else:
  print('forma um triangulo')
