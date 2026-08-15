qp = int(input('Quantas pessoas assistiram a apresentação:'))
cont = 0
contg = 0
contng = 0

while cont <= qp:
    cont += 1
    gostou = input('gostou da apresentação (“sim” ou “não”):')

    if gostou == 'sim':
        contg += 1

    else:
        contng += 1

if contg > contng:
    print('A maioria das pessoas gostaram da apresentação!')

elif contng > contg:
    print('A maioria das pessoas não gostaram da apresentação!')

else:
    print('Deu empate!')
