#um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,lendo o nome deles escrevendo o nome do escolhido
import random 
alunos = []
aluno = input("digite o nome do aluno:")
alunos.append(aluno)
while aluno != 'N':
  aluno = input("digite o nome do aluno:")
  alunos.append(aluno)
  continue
if aluno == 'N':
  print(sorted(alunos))
  print(alunos)
  print(random.choice(alunos))

