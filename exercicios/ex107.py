#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
def aumentar(valor, taxa):
    res = valor + (valor * taxa / 100)
    return res


def diminuir(valor, taxa):
    res = valor - (valor * taxa / 100)
    return res


def dobro(valor):
    res = valor * 2
    return res


def metade(valor):
    res = valor / 2
    return res
