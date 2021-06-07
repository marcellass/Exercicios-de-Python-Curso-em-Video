frase = input().upper()

n = frase.split('A')
p = frase.find('A')
f = frase.rfind('A') #lado direito
 

print(f'A letra A aparece {n} vezes')
print(f'Aparece pela primeira: {p}')
print(f'Aparece pela ultima vez {f}')