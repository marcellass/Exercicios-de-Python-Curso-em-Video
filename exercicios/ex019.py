from random import choice 
nome1 = str(input('Digite o primeiro aluno: '))
nome2 = str(input('Digite o segundo aluno: '))
nome3 = str(input('Digite o terceiro aluno: '))
nome4 = str(input('Digite o quarto aluno: '))

lista  = [nome1,nome2,nome3,nome4]

sorteio = choice(lista)

print(f'Dentre os alunos {nome1}, {nome2}, {nome3} e {nome4}, o sorteado para apagar o quadro foi o(a) aluno(a) {sorteio}')