#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*20)
print('banco cev')
print('='*20)
valor = int(input('qual valor voce que sacar? R$'))
while valor != 0:
  if valor >= 50:
    cedulas50 = valor/50
    valor = valor % 50 
    print('total de {:.0f} de 50'.format(cedulas50))
  elif valor >= 20:
    cedulas20 = valor / 20
    valor = valor % 20
    print('total de {:.0f} de 20'.format(cedulas20))
  elif valor >= 10:
    cedulas10 = valor/10
    valor = valor % 10
    print('total de {:.0f} de 10'.format(cedulas10))
  else:
    cedulas1 = valor/1
    valor = valor % 1
    print('total de {:.0f} de 1'.format(cedulas1))

