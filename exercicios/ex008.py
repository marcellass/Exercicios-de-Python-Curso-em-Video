metros = int(input('Digite o valor em metros: '))

conv_cm = metros * 100
conv_milimetros = metros * 1000
conv_km = metros * 1000
conv_deca = metros / 10
conv_deci = metros * 10
conv_hect = metros / 100

print(f'Segue abaixo a conversão de metros para os valores solicitados (Km, Hect, Decametros, Decimetros, Centimetros e Milimetros)')
print(f'De metros para Hect: {conv_hect}')
print(f'De metros para Decametros: {conv_deca}')
print(f'De metros para Decimetros: {conv_deci}')
print(f'De metros para Centímetros: {conv_cm}') 
print(f'De metros para Km: {conv_km} ') 
print(f'De metros para Milimetros: {conv_milimetros}') 