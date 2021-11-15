#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Indique o primeiro termo da PA: '))
r = int(input('Indique a razão da PA: '))
a1 = p
while p < a1 + 10 * r:
    print(p,'  ', end='')
    p += r