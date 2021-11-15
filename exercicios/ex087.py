#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
soma_pares = 0
soma_terceira = 0
maior = []
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input(f'Digite um número para [{i} , {c}] ->  '))
        if i == 1:
            maior.append(matriz[i][c])
        if c == 2 or c == 2 and i == 1 or c == 2 and i == 2:
            soma_terceira+=matriz[i][c]
        if matriz[i][c] % 2 == 0:
            soma_pares+= matriz[i][c]
print()
for i in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[i][c]:^5}]',end='')
    print()
print()
print(f"A soma dos valores pares da matriz é igual a {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_terceira}")
print(f"O maior número da segunda linha é {max(maior)}")
print()
