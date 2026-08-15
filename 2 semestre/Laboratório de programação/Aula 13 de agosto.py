#.sort()

'''lista = ['João', 'Maria', 'Ana', 'Pedro', 'Daniel', 'Eduardo']

lista.sort()

print(lista)'''

#.sort(reverse = true)

'''lista = ['João', 'Maria', 'Ana', 'Pedro', 'Daniel', 'Eduardo']

lista.sort(reverse = true)

print(lista)'''

#.insert()

'''nums1 = [10, 20, 30]

nums1.insert(2, 25)

print(nums1)'''

#Atividade

'''lista1 = ['arroz', 'feijão', 'leite', 'ovos', 'óleo']
lista2 = ['farinha', 'leite', 'feijão', 'macarrão', 'café']

for i in lista1:
    for j in lista2:
        if i == j:
            lista2.remove(i)

lista1.extend(lista2)
lista1.sort()
print(lista1)'''

#Atividade 2

'''nums1 = [23, 300, 450, 10, 15]
nums2 = [15, 24, 10, 23, 560]

for i in nums1:
    for j in nums2:
        if i == j:
            nums2.remove(j)

nums1.extend(nums2)
nums1.sort()
print(nums1)'''

#Fatiamento de listas
'''lista = [10, 20, 30, 40, 50]
print(lista[3])
print(lista[1:4])'''

#Fatiamento de string
'''nome = 'Paralelepípedo'
print(nome[4:8])
print(nome[1::2])'''

#Métodos em string

'''lista = ['B', 'r', 'u', 'n', 'a']

lista[4] = 'o'

print(lista)'''

#-------------------

'''nome = 'Bruna'
print(nome[4])

nome[4] = 'o'''

#-------------------

'''nome = 'Bruna'
alterado = nome.replace('a', 'o')

print(nome)
print(alterado)'''

#-------------------

'''lista = ['B', 'r', 'u', 'n', 'a']
print(lista.remove('n'))
print(lista)'''

#-------------------

'''nome = 'Bruna'
print(nome.replace('a', 'o'))
print(nome)'''

#.lower(), .upper(0, .title(), .capitalize()

'''nome = 'python'
print(nome.upper())
print(nome.title())'''

'''frase = 'PyThOn é fantastático'
print(frase.lower())
print(frase)
print(frase.replace('Python', 'Java'))'''

'''frase = 'PyThOn é fantastático'
frase = frase.lower()
print(frase.replace('python', 'java'))'''

'''frase = 'PyThOn é fantastático'
print(frase.capitalize())
print(frase.title())'''

#.join()

'''frutas = ['uva' ,'maçã', 'banana']
'#'.join(frutas)
print('#'.join(frutas))'''

#.split()

'''cpf = '123.456.789.90'
lista_cpf = cpf.split('.')
print(lista_cpf)'''

#.strip()

'''nome = '        P Y T H O N    '
print(nome)
print(nome.strip())'''

'''nome = 'amora'
print(nome.strip('a'))'''

'''nome = '          PYTHON'
print(nome.strip().strip('P').lower())'''

#.find()

'''fruta = 'banana'
print(fruta.find('b'))
print(fruta.find('na'))
print(fruta.find('m'))'''

#.count(0

'''fruta = 'banana'
print(fruta.count('a'))'''
