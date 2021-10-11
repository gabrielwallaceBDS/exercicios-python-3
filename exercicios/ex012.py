# faça um algoritimo que leia o preco de um produto e mostre o seu preco com 5% de desconto
preço = float(input("preço do produto: "))
desc = ((preço * 5)/100)-preço 
print("valor do produto {} e com desconto de 5% fica {:.2f}".format(preço, desc))