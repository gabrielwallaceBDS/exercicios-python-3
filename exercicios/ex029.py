#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('digite a velocidade do veiculo '))

if velocidade > 80:
  custo = (velocidade - 80)*7.00
  print('sua multa é de {} tenha mais cuidado'.format(custo))
else:
  print('tudo ok, continuar viagem')