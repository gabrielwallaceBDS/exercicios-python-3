#escreva um programa que leia um valor em metros e exiba o convertido em centimetros em milimetros
# km hm dam m dm cm mm 
medida = float(input("digite uma medida em metros"))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print("medidas convertidas\nkm = {}\nhm = {}\ndam = {}\nMetros = {}\ndm = {:.0f}\ncm = {:.0f}\nmm = {:.0f}".format(km,hm, dam, medida, dm, cm, mm))
