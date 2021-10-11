# ramdomizar a lista
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
