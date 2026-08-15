a = float(input('Informe o primeiro valor do triângulo:'))
b = float(input('Informe o segundo valor do triângulo:'))
c = float(input('Informe o terceiro valor do triângulo:'))

if a >= b + c or b >= a + c or c >= b + a:
    print('Não é triângulo.')

elif a == b == c:
    print('É um triângulo equilátero.')

elif a == b or b == c or a == c:
    print('É um triângulo isósceles.')

else:
    print('É um triângulo escaleno')