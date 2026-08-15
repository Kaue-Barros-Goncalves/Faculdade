cont = 0
menorpeso = 10000000

while cont < 11:
    cont += 1
    peso = float(input('Qual o peso do boi (em kg):'))

    if peso < menorpeso:
        menorpeso = peso

print('O maior peso foi:',menorpeso)