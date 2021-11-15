#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
a = [float(input('Insira um número: ')) for i in range(0, 5)]
print(f'Foram digitados {len(a)} números!')
a.sort(reverse=True)
print(f'Em ordem decrescente {a}')
print(f'O valor 5{" " if  5 in a else " não"}está na lista')