#Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from UtilidadesCeV import myFunctions
# Por opção eu coloquei todas as functions que criamos no módulo "myFunctions" no pacote "utilizadesCeV"

_valor = float(input('Digite o preço em R$ .: '))
myFunctions.resumo(_valor, 50, 10)