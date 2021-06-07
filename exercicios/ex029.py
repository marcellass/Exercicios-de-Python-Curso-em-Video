velocidade = float(input('Qual a velocidade em que o carro está: '))
multa = (velocidade-80 )* 7

if velocidade > 80:
    print(f'Você foi multado, o valor total da multa é {multa:.2f}')
else:
    print('Você está dentro da velocidade')