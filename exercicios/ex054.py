#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = []
menor = []
for i in range (1,8):
  ano = int(input('em que ano nasceu a {}° pessoa: '.format(i)))
  if ano > 2002:
    menor.append(ano)
  else:
    maior.append(ano) 
print('ao todo temos {} pessoas maiores de idade'.format(len(maior)))
print('ao todo temos {} pessoas menores de idade'.format(len(menor)))
print(maior)
print(menor)