#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
r1 = float(input('primeiro lado: '))
r2 = float(input('segundo lado: '))
r3 = float(input('terceiro lado: '))
soma = r1 + r2 < r3 
if soma == False:
  if r1 == r2 and r1 == r3 and r2 == r3:
    print('os seguimentos forman um triangulo do tipo EQUILÁTERO')
  elif r1 != r2 and r1 != r3 and r2 != r3:
    print('os seguimentos forman um triangulo do tipo ESCALENO')
  else:
    print('os seguimentos forman um triangulo do tipo ISÓSCELES')
else:
  print('os seguimentos nao forman um triangulo')
  
  
  