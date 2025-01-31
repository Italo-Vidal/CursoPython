from random import choice

aluno1 = input('Digite seu nome: ')
aluno2 = input('Digite seu nome: ')
aluno3 = input('Digite seu nome: ')
aluno4 = input('Digite seu nome: ')

lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)

print(f'O aluno escolhido foi {sorteio}!')