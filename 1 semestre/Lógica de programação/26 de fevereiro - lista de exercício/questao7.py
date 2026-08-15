idade = int(input('Informe a sua idade:'))
peso = float(input('Informe o seu peso (kg):'))

if idade >= 12:
    
    if peso <= 60:
        print('Deve tomar 30 gotas.')

    elif peso > 60:
        print('Deve tomar 40 gotas.')

elif idade < 12:

    if peso <= 10:
        print('Deve tomar 5 gotas.')

    elif peso < 20:
        print('Deve tomar 10 gotas.')

    elif peso <= 30:
        print('Deve tomar 15 gotas.')

    elif peso > 30:
        print('Deve tomar 20 gotas.')