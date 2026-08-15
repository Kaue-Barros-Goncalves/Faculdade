salario_minimo = float(input('Informe o salário mínimo: R$'))
maior_salario = float('-inf')
soma_salario = 0
nome = input('Nome do operário (Para encerrrar digite "sair"):')

while nome != 'sair':

    pecas_fabricadas = int(input('Quantas peças foram fabricadas:'))

    if pecas_fabricadas <= 100:
        classe = 'A'
        salario = salario_minimo + pecas_fabricadas * 2

    else:
        classe = 'B'
        salario = salario_minimo + pecas_fabricadas * 2.5

    if salario > maior_salario:
        maior_salario = salario

    soma_salario += salario

    print(nome,'-',classe,'- R$',salario)

    nome = input('Nome do operário (Para encerrrar digite "sair"):')

print('Maior salário:',maior_salario)
print('Soma dos salários: R$',soma_salario)