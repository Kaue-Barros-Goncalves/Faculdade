listaNum = []
soma_par = 0

while len(listaNum) < 6:
    num = int(input('Escreva o número:'))
    listaNum.append(num)

    if num % 2 == 0:
        soma_par += num

cont = 0

while cont < len(listaNum):
    print(listaNum[cont])
    cont = cont + 1

print('Os 3 primeiros elementos:',listaNum[0], listaNum [1], listaNum[2])
print('Soma números pares:',soma_par)