n1 = int(input('Escreva o primeiro número:'))
n2 = int(input('Escreva o segundo número:'))
codigo = input('Escreva o código de condição (c ou d):')

if codigo == 'c' and n1 > n2:
    print(n2,',',n1)

elif codigo == 'c' and n2 > n1:
    print(n1,',',n2)

elif codigo == 'd' and n1 > n2:
    print(n1,',',n2)

else:
    print(n2,',',n1)