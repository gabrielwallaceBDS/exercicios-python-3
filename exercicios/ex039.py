#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('ano de nascimento: '))
idade = 2021 - ano
anoatual = 2021
print('quem nasceu em {} tem {} anos em {}'.format(ano,idade, anoatual))
if idade == 18:
  print('voce tem que se alistar IMEDIATAMENTE')
elif idade < 18:
  resta = idade - 18
  print('seu alistamento é daqui a {} anos'.format(resta))
else:
  sobra = idade - 18
  print('seu alistamento foi a {} anos em {}'.format(sobra, (anoatual - sobra)))