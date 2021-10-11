#faça um programa que leia um numero inteiro e mostre sua tabuada
num = int(input("digite um numero"))
vezes = 0
print('-' * 13)
while vezes < 11:
  tab = (num * vezes)
  print("{} x {} = {}".format(num, vezes, tab))
  vezes +=1
print('-' * 13)


