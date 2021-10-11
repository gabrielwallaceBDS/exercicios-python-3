#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input("digite um numero: "))
numeros = str(numero)

print('unidade: {}'.format(numeros[3]))
print('dezena: {}'.format(numeros[2]))
print('centena: {}'.format(numeros[1]))
print('milhar: {}'.format(numeros[0]))