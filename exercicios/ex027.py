#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input("digite um nome: ").split()
last = len(nome) -1
print(nome[0])
print(nome[last])
