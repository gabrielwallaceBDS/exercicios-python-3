#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ['pedra', 'papel' , 'tesoura']
jogador = int (input('''Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura
Qual é a sua jogada?'''))
computador = randint(0,3)
print("computador jogou {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))
if computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
  print('computador ganhou')
elif jogador == computador:
  print('empate')
else:
  print('jogador ganhou')

