import math
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
print('-=' * 20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')