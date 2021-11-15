#Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
def formata_moeda(valor):
    resultado = str(valor).replace('.', ',0')
    return resultado


def aumentar(valor, aumento):
    return formata_moeda(valor + (valor * (aumento / 100)))


def diminuir(valor, reducao):
    return formata_moeda(valor - (valor * (reducao / 100)))


def dobro(valor):
    return formata_moeda(valor * 2)


def metade(valor):
    return formata_moeda(valor / 2)
---------------------------------------------------------------------------------------------------------------------------------------
from exercicio_108 import moeda


preco = float(input("Informe o preço: R$"))


print(f"A metade de R${moeda.formata_moeda(preco)} é R${moeda.formata_moeda(moeda.metade(preco))}")
print(f"O dobro de R${moeda.formata_moeda(preco)} é R${moeda.dobro(preco)}")
print(f"Aumentando 10%, temos R${moeda.aumentar(preco, 10)}")
print(f"Reduzindo 13%, temos R${moeda.diminuir(preco, 10)}")