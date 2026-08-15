print('Questão 1')

'''nome = input('Escreva o seu nome:')
idade = int(input('Escreva a sua idade:'))
print(f'Olá,{nome}!Você tem {idade} anos')'''

print('Questão 2')

'''nome = input('Escreva o seu nome:')
profissao = input('Escreva a sua profissão:')
print(f'Olá,{nome}!você trabalha como {profissao}. Desejamos um ótimo dia!')'''

print('Questão 3')

'''num1 = int(input('Escreva o primeiro número:'))
num2 = int(input('Escreva o segundo número:'))

soma = num1 + num2
print(f'Soma:{soma}')

subtracao = num1 - num2
print(f'Subtração:{subtracao}')

multiplicacao = num1 * num2
print(f'Multiplicação:{multiplicacao}')

divisao = num1 / num2
resto = num1 % num2
print(f'Divisão:{divisao}/Resto da divisão:{resto}')'''

print('Questão 4')

'''celcius = float(input('Insira a temperatura em graus celcius:'))
farenheit = celcius * (9/5) + 32
print(f'Temperatura convertida para farenheit:{farenheit}')'''

print('Questão 5')

'''num = float(input('Escreva um número:'))

if num > 0:
    print(f'Seu número é positivo')

elif num < 0:
    print(f'Seu número é negativo')

else:
    print(f'Seu número é igual a 0')'''

print('Questão 6')

'''num = int(input('Escreva um número inteiro:'))

if num % 2 == 0:
    print(f'O número {num} é par')

else:
    print(f'O número {num} é ímpar')'''

print('Questão 7')

'''num = int(input('Escreva um número inteiro positivo (entre 5 e 50):'))

for i in range(5,num + 1,1):
    print(i)'''

print('Questão 8')

'''n = int(input('Escreva um número de 100 a 500:'))
while n < 100 or n > 500:
    print(f'Número inválido! O número deve ser entre 100 e 500.')
    n = int(input('Escreva um número de 100 a 500:'))
    
soma = 0

for i in range(2, n + 1, 2):
    soma += i

print(f'Soma dos números pares até o número {n}:{soma}')'''

print('Questão 9')

'''temp = float(input('Escreva a temperatura do ambiente atualmente:'))

if temp > 25:
    print(f'Está calor')

elif 15 <= temp and temp <= 25:
    print(f'Está agradável')

else:
    print(f'Está frio')'''

print('Questão 10')

'''nomes = []

for i in range(1, 6, 1):
    nome = input(f'Escreva um nome ({i}):')
    nomes.append(nome)

exibir = input('Exibir nomes? ("s" ou "n"):')

while exibir != 's' and exibir != 'n':
    print(f'Escreva somente "s" ou "n"!'
    exibir = input('Exibir nomes? ("s" ou "n"):')
          
if exibir == 's':
    for nome in nomes:
        print(f'{nome}')

else:
    print(f'Obrigado')'''

print('Questão 11')

'''produtos = []
print('Escreva o nome e o preço de 3 produtos')

for i in range(1, 4, 1):
    nome = input(f'Escreva o nome do produto ({i}):')
    preco = float(input(f'Escreva o preço do produto ({i}):'))
    produtos.append([nome, preco])

for nome, preco in produtos:
    print(f'Produto: {nome} - Preço: R${preco:.2f}')'''

print('Questão 12')

'''lista = [['A', 'B'], ['C'], ['D', 'E', 'F']]

maior_tamanho = 0

for sublista in lista:
    if len(sublista) > maior_tamanho:
        maior_tamanho = len(sublista)

for sublista in lista:
    while len(sublista) < maior_tamanho:
        sublista.append('X')

print(lista)'''

print('Questão 13 - Reescreva os códigos a seguir substituindo o laço while por um laço for')
'''print('a)')

for i in range(1, 11):
    print(f'Número: {i}')

print('b)')

soma = 0

for i in range(2, 21, 2):
    soma += i

print(f'Soma dos pares: {soma}')

print('c)')

valores = [12, 5, 8, 21, 3, 18, 14]

for i in range(len(valores)):
    if valores[i] > 10:
        print(f'Valor maior que 10 encontrado: {valores[i]}')'''

print('Questão 14')
'''print('a)')

cont = 10

while cont > 0:
    print(f'Lançamento em {cont}...')
    cont -= 1
print(f'Decolar!')

print('b)')

frutas = ['maçã', 'Banana', 'Laranja', 'Uva']
cont = 0

while cont < len(frutas):
    print(f'Item: {frutas [cont]}')
    cont += 1'''
