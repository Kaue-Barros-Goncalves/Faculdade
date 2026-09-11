continuar = 's'

while continuar == 's':

    placa = input('Insira uma placa de carro:')
    
    if len(placa) == 8 and placa[:3].isalpha() and placa[3] == '-' and placa[4:].isnumeric():
        print('Sua placa é modelo antigo')

    elif len(placa) == 7 and placa[:3].isalpha() and placa[3].isnumeric and placa[4].isalpha() and placa[5:].isnumeric():
        print('Sua placa é modelo mercosul')

    else:
        print('Sua placa é inválida')

    continuar = input('Deseja continuar ("s" ou "n" para encerrar)?:').lower()
