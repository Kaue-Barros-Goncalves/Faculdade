t = input('Qual o tipo de combustível (gasolina ou álcool):')
l = float(input('Quantidade de litros:'))

if l < 20:
    if t == 'gasolina':
        preco = l * 7
        print('O seu valor é:', preco)

    else:
        preco = l * 5
        print('O seu valor é:', preco)

if 20 <= l <= 30:
    if t == 'gasolina':
        preco = (l * 7) * 0.05
        resultado = l * 7 - preco
        print('O seu valor é:', resultado)
    
    else:
        preco = (l * 5) * 0.05
        resultado = l * 5 - preco
        print('O seu valor é:', resultado)

if l > 30:
    if t == 'gasolina':
        preco = (l * 7) * 0.10
        resultado = l * 7 - preco
        print('O seu valor é:', resultado)

    else:
        preco = (l * 5) * 0.10
        resultado = l * 5 - preco
        print('O seu valor é:', resultado)