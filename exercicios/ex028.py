from random import randint

q = int(input('Try to find the number: '))
x = randint(0,5)

print('PROCESSANDO...')
if q == x: 
    print('You won!')
else:
    print('You lose, the correct number was {x}')

