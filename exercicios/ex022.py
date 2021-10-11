#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input("digite o nome completo: ")).strip
upper = print(nome.upper())
lower = print(nome.lower())
total = nome.replace(" ", "")
print(len(total))
split = nome.split()
print(len(split[0]))