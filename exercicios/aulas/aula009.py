#FATIAMENTO
frase = "curso em video python"
print(frase[9])#imprime o 9° elemnto da frase o 'v'
print(frase[9:13])#do 9 ao 13 'vide'
print(frase[9:21:2])#do 9 ao 21 pulando de 2 em 2 'vdopto'
print(frase[:5])#vai do inicio até 5 'curso'
print(frase[15:])#vai do 15 até o final
print(frase[9::3])#começa em 9 vai até o final pulando de 3 em 3 'veph'

#ANALISE
print(len(frase))#coprimento da frase '21'
print(frase.count('o'))#quantas vezes tem a letra o '3' 
print(frase.count('o',0,13))#o's  entre os caracteres 0 e 13 '1'
print(frase.find('deo'))#indica em qua posiçao tem 'deo' na frase '11'
print(frase.find('android'))# retorna -1 pos nao existe 'android' na frase
print('curso' in frase)#retorna True pois tem 'curso' na frase

#TRANSFORMAÇÃO
print(frase.replace('python','android'))#substitui 'python' da frase por 'android'
print(frase.upper())#coloca a frase inteira em maiusculas
print(frase.lower())#transforma a frase inteira em minusculas
print(frase.capitalize())#joga todos os caracteres para minusculo e somente a primeira letra maiusculas
print(frase.title())#os primeiros caracteres depois dos espaços ficam maiusculas
print(frase.strip())#remove os espaços inuteis do inicio e do começo da frase
print(frase.rstrip())#remove espaços da direita
print(frase.lstrip())#remove espaços da esquerda

#DIVISAO
print(frase.split())#divide a frase onde tem os espaços e tranforma cada parte em string separada
print('-'.join(frase))#coloca o '-' onde tem os espaços


#PRINT
#para diminuir o uso de prints do codigo use 

