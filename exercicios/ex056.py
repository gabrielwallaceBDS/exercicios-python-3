#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
mulheres = 0
idade1 = 0
nome1 = ''
idades = 0
for i in range(1,5):
  print('{}{}°Pessoa{}'.format(5*'=-',i,5*'=-'))
  nome = str(input('Nome: '))
  idade = int(input('Idade: '))
  media += idade
  sexo = str(input('Sexo [M/F]: '))
  if sexo == 'F' or sexo == 'f':
      mulheres +=1
      if idade > idade1:
        idade1 += idade
  if sexo == 'm' or sexo == 'M':
    if idade > idades: 
      idades = idade
      nome1 = nome

print('a media de idade do grupo é {}'.format(media/4))
print('o homem mais velho tem {} e se chama {} '.format(idades,nome1))
print('ao todo sao {} mulheres com menos de {} anos'.format(mulheres, idade1 -1))

