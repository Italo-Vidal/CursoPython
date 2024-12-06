from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hipo = hypot(co, ca)

print('*' * 37)
print(f'O valor da hipotenusa é {hipo:.2f}')