from math import hypot
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adajacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(cateto_oposto,cateto_adajacente)

print('O cálculo final dos dois catetos a) {cateto_oposto} e b) {cateto_adjacente} , dá um resultado da hipotenusa {hipotenusa}')