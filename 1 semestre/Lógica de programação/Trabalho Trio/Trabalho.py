import random

numeros = []
i=0
while i < 10:
    numeros.append(random.randint(-10,10))
    i = i + 1
print("Numeros:", numeros)

#Imprima a soma dos elementos que estão nas posições pares da lista.
soma_par = 0
cont = 0

while cont < len(numeros):
    if cont % 2 == 0:
        soma_par += numeros[cont]
    cont += 1
print('Soma dos números que estão nas posições pares:',soma_par)

# Imprima a lista de trás para frente, sem utilizar índices negativos.
cont = len(numeros) - 1

while cont >= 0:
    print('Números;',numeros[cont])
    cont -= 1

#Imprima o menor número negativo presente na lista. Caso não existam números negativos, informe ao usuário.
cont = 0
menor_numero = 0

while cont < len(numeros):
    if numeros[cont] < menor_numero:
            menor_numero = numeros[cont]
    cont += 1

if menor_numero < 0:
    print('Menor número negativo:',menor_numero)
else:
    print('Não tem número negativo')

# Imprima o maior número entre os armazenados nas 5 primeiras posições da lista.
cont = 0
maior_numero = numeros[cont]

while cont < 5:
    if numeros[cont] > maior_numero:
        maior_numero = numeros[cont]
    cont += 1

print('Maior número entre as 5 primeiras posições:',maior_numero)