lista = [10,5,8,20,50,10,5,8,8,60,10,5,5,3,50]
maior_elemento = 0
soma = 0
cont = 0

while cont < len(lista):

    if lista[cont] > maior_elemento:
        maior_elemento = lista[cont]

    if lista[cont] > 0:
        soma += lista[cont]

    if lista[cont] % 2 == 0:
        print('O número',lista[cont],'é par e está na posição:',cont)

    cont += 1

print('O maior elemento é:', maior_elemento)
print('Soma dos elementos positivos:', soma)

cont = 0
elemento = 1

while cont < 5:
    print('Elemento:', elemento,'- Número:',lista[cont])
    cont += 1
    elemento += 1
    