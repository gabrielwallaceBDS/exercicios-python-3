#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
galera = list()
pessoa = dict()
idade1 = 0
mulheres = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    if pessoa['sexo'] == 'F':
      mulheres+=1
    print('Erro! por favor digite apenas M ou F')
  pessoa['idade'] = int(input('idade: '))
  idade1 += pessoa['idade']
  galera.append(pessoa.copy()) 
  while True:
      resp = str(input('deseja continuar? [S/N]')).upper()[0]
      if resp in 'SN':
        break
      print('responda apenas S ou N')
  if resp == 'N':
    break
print(galera)
print(f'o numero de pessoas cadastradas é de {len(galera)}')
print(f'a media das idades é {idade1/len(galera)}')

 
