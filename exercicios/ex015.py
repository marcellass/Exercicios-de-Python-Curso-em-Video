dias = int(input('Quantos dias foi alugado? '))
km_rodado = float(input('Quantos Km rodado? '))

pago = (dias * 60) + (km_rodado * 0.15)


print(f'O total a pagar é de R$ {pago}')