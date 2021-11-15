#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
tupla = (int(input('digite um valor: ')),
int(input('digite outro valor: ')),
int(input('digite mais um valor: ')),
int(input('digite o ultimo valor: '))
)
print(f'voce digitou os valores {tupla}')
print(f'o valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
  print(f'o valor 3 apareceu na posicao {tupla.index(3)+1}')
else:
  print('nao tem numero 3 na tupla')
print('os numeros pares digitados sao: ',end = '')
for n in tupla:
  if n % 2 == 0:
    print(n,end = ' ')


