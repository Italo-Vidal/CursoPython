num = int(input('Digite um número: '))

cont = 1
print('-' * 12)
while cont <= 10:
    print(f'{num} x {cont:2} = {num * cont}')
    cont += 1
print('-' * 12)
