#crie um algoritimo que leia um numero e mostre o seu dobro triplo e sua raiz quadrada
import math
numero = int(input("digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = int(math.sqrt(numero))
print("o numero digitado é {} seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}".format(numero, dobro, triplo, raiz))