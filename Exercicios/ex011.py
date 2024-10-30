largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print('A área da parede é de {}m². \nPara pintar essa parede você necessita de {:.2f} Litros de tinta!'.format(area, tinta))
