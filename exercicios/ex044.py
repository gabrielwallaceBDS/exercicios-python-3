#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
x = '=' * 16
print('{}Maggicz7 Shop{}'.format(x,x))
preço = float(input('digite o valor da compra: '))
print('''[1] à vista dinheiro/cheque: 10% de desconto 
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')
opçao = int(input('opção de pagamento: '))
if opçao == 1:
  final = preço -((preço * 10)/100) 
  print ('sua compra de {} vai custar {} no final a vista no dinheiro/cheque!'.format(preço, final))
elif opçao == 2:
  final = preço -((preço * 5)/100)
  print ('sua compra de {} vai custar {} no final no cartao a vista!'.format(preço, final).format(preço, final))
elif opçao == 3:
  final = preço/2
  print ('sua compra de {} vai custar 2x R${}!'.format(preço, final).format(preço, final))
elif opçao == 4:
  vezes = int(input('quantas parcelas: '))
  final = preço +((preço * 20)/100)
  parc = final / vezes
  print('a sua compra de {} vai ficar {} no total em {} vezes com parcelas de {}'.format(preço, final,vezes, parc ))
