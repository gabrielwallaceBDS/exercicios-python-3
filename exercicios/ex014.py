#crie um programa que converta graus em Fahrenheit
graus = float(input("digite os graus: "))
Fahrenheit = (graus * 1.8) + 32
print("{:.1f}°C convertidos sao {:.1f}F°".format(graus,Fahrenheit))