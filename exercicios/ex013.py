salario_atual = float(input('Qual o seu salário atual: '))
aumento = salario_atual * 15 / 100
salario_aumento = salario_atual + aumento 

print(f'Antigamente o seu saláro era R${salario_atual:.2f} porém estamos disponibilizando 15% de aumento, totalizando {salario_aumento:.2f}')
