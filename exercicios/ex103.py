#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado 
def ficha(nome = 'desconhecido', gol = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = '0'
    return f'O jogador {nome} fez {gol} gols no campeonato'

jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
print(ficha(jogador, gols))