#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo :'))
razao = int(input('razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while cont <= total:
    print('{} -> '.format(termo),end = '')
    termo += razao
    cont += 1
  print('PAUSA')
  mais = int(input('quantas vezes voce quer mostrar a mais? '))
print('progesso finalizado com {} termos'.format(total))