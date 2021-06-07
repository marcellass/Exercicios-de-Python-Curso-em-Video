preco = float(input('Qual o preço do produto: '))

desconto = (preco * 5/ 100)
novo_preco = preco - desconto

print(f'O valor do produto é R$ {preco:.2f} porém com 5% de desconto o valor dele vai para R${novo_preco:.2f}')