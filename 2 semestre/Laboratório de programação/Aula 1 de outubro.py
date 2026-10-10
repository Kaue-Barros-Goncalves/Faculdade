'''def saudar (nome = 'padrão', idade = 18):
    print('-'*50)
    print(f'Olá {nome}, você tem {idade} anos')

print(saudar('Maria', 72))

saudar(34, 'Carlos')

saudar('João')

saudar()'''

'''def somar (x, y):
    return x + y

def subtrair (x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir (x, y):
    if y != 0:
        return x / y
    return 'Não existe divisão por zero'


print(somar(10, 5))

print(subtrair(10, 5))

print(multiplicar(10, 5))

print(dividir(10, 5))

print('*********')

print(somar(10, 0))

print(subtrair(10, 0))

print(multiplicar(10, 0))

print(dividir(10, 0))'''

'''def eh_par (num):
    return num % 2 == 0


print(eh_par(23))
print(eh_par(22))

nums = [11, 13, 45, 44, 42, 102]

for num in nums:
    if eh_par(num):
        print(f'{num} é par')

    else:
        print(f'{num} é ímpar')'''

'''def faixa_etaria (idade):
    if idade <= 12:
        return 'criança'
    if idade <= 18:
        return 'adolescente'
    if idade <= 60:
        return 'adulto'
    return 'idoso'


print(faixa_etaria(8))
print(faixa_etaria(82))
print(faixa_etaria(66))'''
