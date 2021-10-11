#faça algoritimo que leia o salario do funcionario e faça um ajuste salarial de 15% de aumento
salario = float(input("digite seu salario: "))
reajuste = ((salario * 15)/100)+salario
print("salario de {} com reajuste de 15% fica {:.2f} ".format(salario, reajuste))