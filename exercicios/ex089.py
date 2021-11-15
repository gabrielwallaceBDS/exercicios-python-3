#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
print('\33[34m-='*53)
print(f'\33[32m{"Avaliando alunos":^106}')
print('\33[34m-='*53)
li = [[], [[], [], []]]
escolha = c = mostrar = 0
while escolha != 'n':
    escolha = 0
    li[0].append(input('\33[35mNome: '))
    n1 = float(input('\33[35mNota 1: '))
    n2 = float(input('Nota 2: '))
    li[1][0].append(n1)
    li[1][1].append(n2)
    li[1][2].append((n1+n2)/2)
    while escolha != 'n' and escolha != 's':
        escolha = input('\33[35mQuer continuar [S/N]? ').lower().strip()
print('\33[36m-='*15)
print(f'\33[33mNº \33[36m/\33[34m   NOME    \33[36m/\33[32m    {"MEDIA":>}')
print('\33[36m=='*15)
for v in li[0]:
    print(f'\33[33m{c}', end='\33[36m /')
    print(f'\33[34m{v:^11}', end='\33[36m /')
    print(f'\33[32m{li[1][2][c]:^13.1f}')
    c += 1
print('\33[36m-='*15)
while mostrar != 999:
    mostrar = int(input('\33[35mMostrar notas de qual aluno? (999 para encerrar): '))
    if c > mostrar >= 0:
        print(f'\33[35mAs notas de \33[34m{li[0][mostrar]}\33[35m são \33[32m{li[1][0][mostrar]}\33[35m e \33[32m{li[1][1][mostrar]}')
        print('\33[36m-='*15)
print('\33[35mPrograma encerrado :) obrigado por participar do Boletim...')