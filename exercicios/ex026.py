#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input("digite uma frase: ").strip()
frase = frase.upper()
print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))
