#crie um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preco a pagar . sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado
km = int(input("km percorridos"))
dias = int(input("dias que foram utilizados o carro"))
total = (km * 0.15) + (dias * 60)
print("o total a pagr é de {}".format(total))