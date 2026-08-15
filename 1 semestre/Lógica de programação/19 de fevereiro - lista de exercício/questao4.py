num = int(input('Digite um valor:'))

if num > 0:
    print('Positivo')
    print('O dobro do seu valor é:',num * 2)

elif num < 0:
    print('Negativo')

    if num % 2 == 0:
        print('O seu valor é par')

    else:
        print('O seu valor é ímpar')
else:
    print('O seu valor é 0')
