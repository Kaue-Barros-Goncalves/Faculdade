num = float(input('Insira o número (0 para encerrar):'))
listaNum = []

while num != 0:
    listaNum.append(num)
    num = float(input('Insira o número (0 para encerrar):'))

print('Lista:', listaNum)
print('Tamanho da lista:', len(listaNum))

cont = 0

while cont < len(listaNum):
    print(listaNum[cont])
    cont = cont + 1