n1 = int(input('Escreva o primeiro número:'))
n2 = int(input('Escreva o segundo número:'))
d = 0

if n2 == 0:
    print('Não pode ser feita divisão por zero!')

else:
    d = n1 / n2
    print('Resultado igual a:',d)