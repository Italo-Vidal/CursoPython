from math import radians, sin, cos, tan

ang = float(input('Digite o valor do angulo: '))

grau = radians(ang)

seno = sin(grau)
cosseno = cos(grau)
tangente = tan(grau)

print(f'O ângulo de {ang:.2f}º tem \nO SENO de {seno:.2f} \nO COSSENO de {cosseno:.2f} \nE a TANGENTE de {tangente:.2f}')