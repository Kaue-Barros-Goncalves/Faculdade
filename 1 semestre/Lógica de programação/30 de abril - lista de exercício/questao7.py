lista = []
cont = 0

while cont < 10:
    cont += 1
    numero = int(input('Insira um número:'))
    lista.append(numero)

aux = lista[0]
lista[0] = lista[-1]
lista[-1] = aux

print("Lista com elementos trocados:",lista)