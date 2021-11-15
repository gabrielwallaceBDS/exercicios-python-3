#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []
while True:
    num = int(input('Digite um número inteiro: '))
    a = lista.count(num)
    if a == 0:
        lista.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Você já adicionou esse número...')
    resp = str(input('Quer continuar?[S/N] '))
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
novalista = sorted(lista)
print(f'Os números que você digitou foram:{novalista}')