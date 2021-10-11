#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo e todas as infrmacoes possiveis sobre ele 
algo = input("digite qualquer coisa: ")
tipo = type(algo)

print("o {} é do tipo {}".format(algo,tipo))
print("tem numeros? :",algo.isalnum())
print("tem é da tabela ascii: ", algo.isascii())
