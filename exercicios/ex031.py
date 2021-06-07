distancia = int(input('Digite a distância: '))


if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print(f'Sua passagem deu um total de R${preco:.2f}')