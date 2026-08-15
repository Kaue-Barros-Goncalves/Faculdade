cont_agua = 0
cont_refri = 0
cont_suco = 0
total_conta = 0
bebida = input('Informe qual a bebida (água, refrigerante, suco) (para encerrar digite "sair"):')

while bebida != 'sair':

    quant = int(input('Informe a quantidade:'))

    if bebida == 'água':
        cont_agua += quant
        total_conta += quant * 2

    elif bebida == 'refrigerante':
        cont_refri += quant
        total_conta += quant * 3

    elif bebida == 'suco':
        cont_suco += quant
        total_conta += quant * 4

    else:
        print('Bebida inválida!')

    bebida = input('Informe qual a bebida (água, refrigerante, suco) (para encerrar digite "sair"):')

print('Valor total da conta:',total_conta)
print('Quantidade de água:',cont_agua)
print('Quantidade de refri:',cont_refri)
print('Quantidade de suco:',cont_suco)