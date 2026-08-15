lista = []
numeros = int(input('Insira um número (0 para encerrar):'))

while numeros != 0:
    lista.append(numeros)
    numeros = int(input('Insira um número (0 para encerrar):'))

print('Lista original:',lista)

cont = 0

while cont < len(lista):
    lista[cont] = lista[cont] * -1
    cont += 1

print('Lista com sinal trocado:',lista)