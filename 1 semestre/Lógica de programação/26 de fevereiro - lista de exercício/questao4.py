n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))

if n1 != 0 and n2 != 0 and n3 != 0:
    print('Todos os números são diferentes de zero')

    if n1 > 0 and n2 > 0 and n3 > 0:
        result = n1 * n2 * n3
        print('Resultado:', result)

    elif n1 > 0 or n2 > 0 or n3 > 0:
        result = n1 + n2 + n3
        print('Resultado:', result)

    elif n1 < 0 and n2 < 0 and n3 < 0:
        result = (n1 + n2 + n3) * 3
        print('Resultado:', result)

else:
    print('Todos os números devem ser diferentes de zero.')