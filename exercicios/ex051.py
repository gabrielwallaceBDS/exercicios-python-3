#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('''
=============================
   10 termos de uma PA
=============================
''')
termo = int(input('primeiro termo: '))
razao = int(input('razao: ')) 
dez = termo + (11 - 1) * razao
for c in range(termo,dez, razao):
  print('{} '.format(c), end='→ ')
print('acabou')