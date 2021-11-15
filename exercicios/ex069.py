#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
continuar = 'S'
maior = mulher = homem = 0
while continuar == 'S':
  print('-'*20)
  print('cadastre uma pessoa')
  print('-'*20)
  idade = int(input('idade: '))
  if idade > 18:
    maior+=1
  sexo = str(input('sexo[M/F]: ')).upper()
  if sexo == 'M':
    homem+=1
  if sexo == 'F' and idade < 20:
    mulher +=1
  print('-'*20)
  continuar = str(input('Quer continuar? [S/N]: ')).upper()
  if continuar == 'N':
    break
print(f'total de pessoas com mais de 18 anos: {maior}')
print(f'ao todo temos {homem} homem cadastrado')
print(f'e temos {mulher} mulher com menos de 20 anos')

