nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

contar = nome.split()

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome é {contar[0]} e ele tem {len(contar[0])} letras')
