#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.
brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('\n{:=^30}'.format(' BRASILEIRÃO 2018 '))
print('''\nEscolha uma das opções abaixo para exibir:
[ A ] Os 5 primeiros
[ B ] Os últimos 4 colocados
[ C ] Times em ordem alfabética
[ D ] Em que posição o Chapecoense
[ E ] Sair''')
while True:
    opcao = str(input('Digite a opção desejada: ')).upper().strip()
    if opcao == 'A':
        for c in (brasileirão[0:5]):
            print(c)
    elif opcao == 'B':
        print(brasileirão[-4:])
    elif opcao == 'C':
        print(sorted(brasileirão))
    elif opcao == 'D':
        print('O Chapecoense entá em {}°.'.format(brasileirão.index('Chapecoense')+1))
    elif opcao == 'E':
        break