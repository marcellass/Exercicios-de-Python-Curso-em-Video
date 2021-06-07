salario = float(input('Digite o seu sálario: '))


if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} reais passa a ganhar {novo:.2f}')