#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
peso = float (input('digite seu peso: '))
altura = float(input('digite a altura: '))
imc = peso/(altura ** 2)
if imc < 18.5:
  print('abaixo do peso imc = {:.1f}'.format(imc))
elif imc > 18.5 and imc < 25:
  print('peso ideal imc = {:.1f}'.format(imc))
elif imc > 25 and imc < 30:
  print('sobrepeso imc = {:.1f}'.format(imc))
elif imc > 30 and imc < 40:
  print('obesidade imc = {:.1f}'.format(imc))
elif imc < 40:
  print('obesidade morbida imc = {:.1f}'.format(imc))