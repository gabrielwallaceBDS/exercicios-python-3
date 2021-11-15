#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import random
from time import sleep
jogos = int(input('quantos jogos voce deseja fazer? '))
numeros = []
jogo = 0
for i in range(0, jogos):
  while True:
    n1 = random.randint(1,60)
    numeros.append(n1)
    if len(numeros) == 6:
      break
  jogo+=1
  print(f'jogo {jogo}: {sorted(numeros)}')
  sleep(1)
  numeros.clear()
  if jogo == jogos:
    break
 


  
