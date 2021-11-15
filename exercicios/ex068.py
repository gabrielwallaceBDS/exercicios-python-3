#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('vamos jogar PAR ou IMPAR')
while True:
  player = int(input('diga um valor: '))
  PorI = str(input('Par ou Impar? [P/I]: ')).upper()
  comp = randint(0,11)
  total = player + comp
  if total % 2 == 0 and PorI == 'P':
    print (f'voce jogou {player} e o computador jogou {comp}. Total de {total} deu Par ')
    print('voce venceu!')
  else:
    print('voce perdeu!!')
    print(comp)
    