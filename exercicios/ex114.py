#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
  site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.erros.URLError:
  print('O site pudim nao esta acessivel!')
else:
  print('o site esta acessivel')
  

  