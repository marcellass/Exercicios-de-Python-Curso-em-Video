nome = input('Digite seu nome: ').strip()

p = nome.lstrip()
f = nome.rfind()


print(f'Seu nome é: {nome}')
print(f'O primeiro nome é: {p}')
print(f'O ultimo nome é: {f}')