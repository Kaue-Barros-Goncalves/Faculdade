tc = input('Tipo de consumidor (residencial/comercial/industrial:)')
ca = float(input('Escreva o seu consumo de água em m³:'))

if tc == 'residencial':
    calculo = (ca * 0.05) + 5
    print('O valor a ser pago é:', calculo)

elif tc == 'comercial':
    if ca <= 80:
        print('O valor a ser pago é: 500')

    else:
        calculo = 500 + (ca - 80) * 0.25
        print('O valor a ser pago é:',calculo)

elif tc == 'industrial':
    if ca <= 100:
        print('O seu valor a ser pago é: 800')

    else:
        calculo = 800 + (ca - 100) *0.04
        print('O valor a ser pago é:',calculo)