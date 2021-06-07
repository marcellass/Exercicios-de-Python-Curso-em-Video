largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))

area = altura * largura 
litro = area / 2
print(f'Sua parede tem a dimensão    {largura}x{altura}')
print(f'A área da parede é {area}m² e é necessário {litro}L de tinta para pintá-la')