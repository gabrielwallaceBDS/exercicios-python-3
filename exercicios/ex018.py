#calcule o seno o coseno e a tangente com o angulo

import math
angulo = float(input("digite o angulo: "))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O angulo de {} tem o SENO de {:.2f}\nO angulo de {} tem o COSENO de {:.2f}\nO angulo de {} tem o TANGENTE de {:.2f}".format(angulo,seno,angulo,coseno,angulo,tangente))

