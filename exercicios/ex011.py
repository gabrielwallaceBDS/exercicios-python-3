#faça um programa que leia a largura e a altura de uma parede em metros calcule a sua area e a quantidade de tinta necessaria para pintala sabendo que cada litro de tinta pinta 2m² 
largura = float(input("digite a largura da parede: "))
altura = float(input("digite a altura da parede: "))
m = altura * largura
litros = m / 2
print("a parede de {}x{} tem {}m² e utilizara {:.2f}Litros de tinta para ser pintada ".format(largura, altura, m, litros))