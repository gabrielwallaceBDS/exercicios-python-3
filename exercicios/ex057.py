#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('informe seu sexo')).strip().upper()[0]
while sexo not in 'MmFf':
  print('dados invalidos.Digite seu sexo')
  sexo = str(input('informe seu sexo')).upper()
print('sexo {} registrado com sucesso'.format(sexo))

