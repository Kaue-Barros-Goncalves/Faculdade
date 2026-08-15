lista = [-5,10,-8,-3,5,10,11,8,-9,10]
positivo = []
negativo = []
cont = 0

while cont < len(lista):

    if lista[cont] >= 0:
        positivo.append(lista[cont])

    else:
        negativo.append(lista[cont])

    cont += 1

print('Números positivos:',positivo)
print('Números negativos:',negativo)