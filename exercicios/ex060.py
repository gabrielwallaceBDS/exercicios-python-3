#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
fatorial = int (input("written number for your fatorial:"))
count = fatorial
f = 1
for c in range(1, count+1, +1):
    f*=c
print(f)