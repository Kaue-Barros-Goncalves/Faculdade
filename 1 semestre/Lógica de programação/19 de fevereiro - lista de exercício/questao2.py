lado1 = int(input('Escreva o primeiro lado:'))
lado2 = int(input('Escreva o segundo lado:'))
if lado1 == lado2:
    print('Quadrado perfeito')
    
else:
    print('Retângulo')

    if lado1 > lado2:
        print(lado1,'é maior')

    else:
        print(lado2,'é maior')