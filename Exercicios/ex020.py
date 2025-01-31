from random import shuffle

aluno1 = str(input('Digite seu nome: '))
aluno2 = str(input('Digite seu nome: '))
aluno3 = str(input('Digite seu nome: '))
aluno4 = str(input('Digite seu nome: '))

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print('—' * 30)
print('A ordem de apresentação será')
print('—' * 30)
print(lista)
print('—' * 30)