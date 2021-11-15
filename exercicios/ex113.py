#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
              print('\033[31mErro! Por favor, digite um número, inteiro, válido.\033[m')
              continue
        except (KeyboardInterrupt):
              print('O usuário preferiu não digitar este número.')
              return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg)).real
        except (ValueError, TypeError):
              print('\033[31mERRO! Por favor, digite um número, REAL, válido.\033[m')
              continue
        except (KeyboardInterrupt):
               print('O usuário preferiu não digitar este número REAL.')
               return 0
        else:
            return n


# Principal
num = leiaInt('Digite um número INTEIRO: ')
print(f'O número digitado foi {num}.')

numr = leiafloat('Digite um núremo REAL: ')
print(f'O número REAL digitado foi: {numr}')