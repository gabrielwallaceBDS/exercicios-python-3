'''cores no terminal Ansi escape sequence
CODIGOS DE STYLE
0(nada)
1(negrito)
3(underline_)
7(invertido)

CODIGOS DE TEXT
30(branco)
31(vermelho)
32(verde)
33(amarelo)
34(azul)
35(roxo)
36(ciano)
37(cinza)
CODIGO DE BACKGROUND
40(branco)
41(vermelho)
42(verde)
43(amarelo)
44(azul)
45(roxo)
46(ciano)
47(cinza)

\033[fonte;texto;background m'''
print('\033[0;30;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[30;42mTESTE\033[m')
print('\033[mTESTE\033[m')
print('\033[7;30mTESTE\033[m')
