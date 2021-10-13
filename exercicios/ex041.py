#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
ano = int(input('digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 9 :
  print('mirin')
elif 9 < idade and idade  < 14:
  print('infantil')
elif 14 < idade and idade < 19:
  print('junior')
elif 19 < idade and idade < 25:
  print('senior')
elif idade > 25:
  print('master')
print('idade atual {}'.format(idade))