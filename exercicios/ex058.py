#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
tentativas = 0
num = randint(0,10)
resp = 0
while resp != num:
  resp = int(input('digite outro numero: '))
  if resp > num:
    print('menos...tente mais uma vez')
  elif resp < num:
    print('mais... tente um numero maior')
  tentativas +=1
print('acertou com {} tentativas'.format(tentativas))
