cont = 0
c0 = 0
cn = 0
soma = 0
negativo = 0

while cont < 6:
    cont += 1
    num = int(input('Informe o seu número inteiro:'))

    if num < 0:
        print('Seu número é negativo!')
        negativo += num
        cn += 1

    elif num > 0:
        print('Seu número é positivo!')
        soma += num

    else:
        print('Seu número é igual a 0!')
        c0 += 1


print('A quantidade de zeros digitados foi:',c0)
print('A soma dos números positivos foi:',soma)
print('A média dos números negativos foi',negativo / cn)