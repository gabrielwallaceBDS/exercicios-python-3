#calcule a hipotenusa com o cateto oposto e cateto adjacente
catop = float(input("digite o cateto oposto: "))
catadj= float(input("digite o cateto adjacente: "))
hipt = ((catop * catop)+(catadj * catadj))**0.5

print("cateto oposto = {}\ncateto adjacente = {}\nhipotenusa = {:.2f}".format(catop,catadj,hipt))