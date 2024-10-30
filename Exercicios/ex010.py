real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 5.60
euro = real / 6.09

print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
print(f'Com R${real:.2f} você pode comprar EU${euro:.2f}')
