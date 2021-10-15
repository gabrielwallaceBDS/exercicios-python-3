#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
Vcasa = float(input('valor da casa: '))
salario = float(input('salario: '))
anos = int(input('anos para pagar: '))

porcSalario = (salario * 30)/100

anosporc = Vcasa / (anos * 12) 

if anosporc > porcSalario:
  print('para pagar uma casa de {:.2f} em {} a prestação sera de {:.2f} \nemprestimo NEGADO'.format(Vcasa,anos,anosporc))
else:
  print('para pagar uma casa de {:.2f} em {} a prestação sera de {:.2f} \nemprestimo CONCEDIDO'.format(Vcasa,anos,anosporc))