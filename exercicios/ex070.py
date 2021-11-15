#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
print('-' *20)
print(' loja super baratao')
print('-' *20)
continuar = 'S'
preco1= caro= barato= cont= 0
nomebarato = ''
preco2 = preco1
while continuar not in 'Nn':
  nome = str(input('nome do produto: '))
  preco = float(input('preço R$: '))
  continuar = str(input('quer continuar? [S/N]')).upper()
  preco1 = preco1 + preco
  cont+=1
  if preco > 1000.00:
    caro+=1 
  nomebarato = nome
  if cont == 1:
    preco2 = preco
    nomebarato = nome
  if preco < preco2:
    preco2 = preco
    nomebarato = nome
print(f'o total da compra foi {preco1}')
print(f'temos {caro} produto custando mais de 1000.00')
print(f'o produdo mais barato foi {nomebarato} que custa R${preco2}')

