salario = float(input('Qual é o slário do Funcionário? R$'))

aumento = salario + (salario * 15 / 100)

print(f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}')
