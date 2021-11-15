#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime
now = datetime.now()
ano = now.year
def voto(nasc):
	"""
	idade = maior ou igual a 18 (e) menor que 70 - obrigatorio
	idade = menor que 18 e maior ou igual a 16 (e) maior que 70 - opcional
	idade = menor que 16 - negado
	"""
	idade = ano - nasc
	print(f"Com {idade} anos, o voto é: ", end=" ")
	if idade >= 18 and idade <= 70:
		print("VOTO OBRIGATORIO!")
	elif idade > 70:
		print("VOTO OPCIONAL!")
	elif idade < 18:	
		print("VOTO NEGADO!")
	
print("-"*20)
voto(int(input("Em que ano você nasceu? ")))
