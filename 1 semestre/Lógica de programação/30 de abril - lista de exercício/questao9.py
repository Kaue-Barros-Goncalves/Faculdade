num = []
par = []
impar = []
cont = 0

while cont < 20:
    numero = int(input('Insira um número:'))
    num.append(numero)
    cont += 1

print('Lista dos númmeros:', num)

aux = 0

while aux < len(num):
    if aux %2 == 0:
        par.append(num[aux])

    else:
        impar.append(num[aux])

    aux += 1
    
print('Lista dos números em posições pares:', par)
print('Lista dos números em posições ímpares:', impar)