#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
p = ('bola', 'amarelo', 'feijao', 'azul', 'bianca', 'macaco', 'hepaminondas', 'brasil','ribeirao preto')
v = 'a', 'e', 'i', 'o', 'u'
for i in range (0, len(p)):
    print(f'\nEm {p[i].upper()} existem as seguintes vogais:', end = ' ')
    for k, vogal in enumerate(v):
        if vogal in p[i]:
            print('{} '.format(v[k]), end = '')