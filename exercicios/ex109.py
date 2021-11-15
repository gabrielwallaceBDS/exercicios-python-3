#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.monetario(valor, "R$")} é {moeda.metade(valor, formato=True)}')
print(f'O dobro de {moeda.monetario(valor)} é {moeda.dobro(valor, formato=True)}')
print(f'Aumentando 10% de {moeda.monetario(valor)}, temos {moeda.aumentar(valor, 10, formato=True)}')
print(f'Reduzindo 13% de {moeda.monetario(valor)}, temos {moeda.diminuir(valor, 13, formato=True)}')


def monetario(num=0.0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')


def metade(num, formato=False):
    resultado = num / 2
    if formato:
        return monetario(resultado)
    else:
        return resultado


def dobro(num, formato=False):
    resultado = num * 2
    if formato:
        return monetario(resultado)
    else:
        return resultado


def aumentar(num, aum, formato=False):
    aumento = ((num * aum) / 100) + num
    if formato:
        return monetario(aumento)
    else:
        return aumento


def diminuir(num, aum, formato=False):
    resultado = num - ((num * aum) / 100)
    if formato:
        return monetario(resultado)
    else:
        return resultado
