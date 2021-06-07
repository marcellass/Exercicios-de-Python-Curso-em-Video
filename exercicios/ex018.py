from math import radians, sin, cos, tan
n = float(input('Digite um ângulo: '))

#Tem que converter para radianos
seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))


print(f'O seno do número informado é {seno:.2f}')
print(f'O cosseno do número informado é {cosseno:.2f}')
print(f'A tangente do número informado é {tangente:.2f}')