#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def titulo(texto):
    print('~'*len(texto)*2)
    print(texto.center(len(texto)*2,' '))
    print('~'*len(texto)*2)

msg = str.title(input('Informe uma mensagem: '))
titulo(msg)