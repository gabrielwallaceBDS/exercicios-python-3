#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
frase = input("digite o nome da cidade: ").upper()
#frase1 = frase.strip()
print('SANTO' in frase.strip()[0:5])
