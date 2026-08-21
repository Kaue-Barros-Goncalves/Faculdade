#Índices negativos

'''frutas = ['maçã', 'banana', 'uva', 'laranja']

print(frutas[-1])
print(frutas[-2])'''

#.insert()

'''frutas = ['maçã', 'uva']

frutas.insert(3, 'banana')
frutas.insert(-10, 'caju')

print(frutas)'''

#Duas variáveis aparentemente iguais

'''lista2 = lista1

print(lista1)
print(lista2)

print('Modificando uma delas:')

lista2[0] = 100

print(lista1)
print(lista2)

print('Usando id()')

print(id(lista1))
print(id(lista2))'''

#Opeador is

'''lista1 = [10, 20, 30]
lista2 = lista1

print(lista1 is lista2)'''

#== verus is

'''lista2 = lista1

print(lista1 is lista2)
print(lista1 == lista2)

print('Exemplo:')

lista1 = [10, 20, 30]
lista2 = lista1
lista3 = [10, 20 ,30]

print(lista1 == lista2)
print(lista1 is lista2)
print(lista1 == lista3)
print(lista1 is lista3)'''

#copy()

'''lista1 = [10, 20 ,30]
lista2 = lista1.copy()

lista2[0] = 100

print(lista1)
print(lista2)

print('Comparando conteúdo e identidade após cópia:')

lista1 = [10, 20 ,30]
lista2 = lista1.copy()

print(lista1 is lista2)
print(lista1 == lista2)
print(id(lista1))
print(id(lista2))

print('Cópia com fatiamento:')

lista1 = [10, 20 ,30]
lista2 = lista1[:]

lista2[0] = 100

print(lista1)
print(lista2)

print('Cópia com list():')

lista1 = [10, 20 ,30]
lista2 = list(lista1)

lista2[0] = 100

print(lista1)
print(lista2)'''

#Shallow copy (cópia rasa) e deep copy (cópia profunda)

'''print('Shallow copy:')

lista1 = [['Ana', 8],
          ['João', 7]]

lista2 = lista1.copy()

lista2[0][1] = 10

print(lista1)
print(lista2)

print('Deep copy:')

import copy

lista1 = [['Ana', 8],
          ['João', 7]]

lista2 = copy.deepcopy(lista1)

lista2[0][1] = 10

print(lista1)
print(lista2)'''

#Removendo um elemento e retornando - pop()

'''frutas = ['maçã', 'banana', 'uva', 'laranja']

fruta = frutas.pop(1)

print(frutas)
print(fruta)'''

#del

'''frutas = ['maçã', 'banana', 'uva', 'laranja']

del frutas[1]

print(frutas)

print('Removendo um intervalo:')

numeros = [10, 20 ,30 ,40, 50]

del numeros[1:4]

print(numeros)'''

#clear()

'''numeros = [10, 20, 30]

numeros.clear()

print(numeros)

print('Ligando clear() ao conceito de memória:')
print('Exemplo 1:')
lista1 = [1, 2, 3]
lista2 = lista1

lista1.clear()

print(lista1)
print(lista2)

print('Exemplo 2:')

lista1 = [1, 2, 3]
lista2 = lista1

lista1 = []

print(lista1)
print(lista2)'''

#Localização e contagem - index

'''frutas = ['maçã', 'banana', 'uva', 'banana']

posicao = frutas.index('banana')

print(posicao)

print('Index(valor,início):')

posicao1 = frutas.index('banana')

posicao2 = frutas.index('banana', posicao1 + 1)

print(posicao2)

print('index() procuando valor inexistente:')

frutas = ['maçã', 'banana', 'uva', 'banana']

posicao = frutas.index('pera')

print(posicao)'''

#in

'''frutas = ['maçã', 'banana', 'uva', 'banana']

print('banana' in frutas)
print('melancia' in frutas)

print('Verificando antes de procurar:')

frutas = ['maçã', 'banana', 'uva', 'banana']
fruta = 'melancia'

if fruta not in frutas:
    print('Fruta não encontrada')

else:
    print(frutas.index(fruta))'''

#reverse()

'''numeros = [10, 20, 30]

numeros.reverse()

print(numeros)

print('reverse() versus [::-1]:')

numeros = [10, 20, 30]
nova = numeros [::-1]

print(numeros)
print(nova)'''

#sort()

'''numeros = [30, 10, 50, 20, 40]
numeros.sort()

print(numeros)

print('sort() ao contrário:')

numeros = [30, 10, 50, 20, 40]
numeros.sort(reverse = True)

print(numeros)'''

#sort() versus sorted()

'''numeros = [30, 10, 50, 20]

nova = sorted(numeros)

print(numeros)
print(nova)'''

#Percorrendo listas - for

'''frutas = ['maçã', 'banana', 'uva']

for fruta in frutas:
    print(fruta)

print('Usando índice:')

frutas = ['maçã', 'banana', 'uva']

for i in range(len(frutas)):
    print(i, frutas[i])'''

#enumerate()

'''frutas = ['maçã', 'banana', 'uva']

for i, fruta in enumerate(frutas):
    print(i, fruta)'''
