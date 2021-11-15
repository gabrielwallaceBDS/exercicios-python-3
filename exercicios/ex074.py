#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print(f'maior numero é {max(tupla)}')
print(f'menor numero é {min(tupla)}')
print(tupla)

