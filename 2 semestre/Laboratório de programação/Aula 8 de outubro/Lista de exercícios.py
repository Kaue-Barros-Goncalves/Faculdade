'''print('Questão 1')

def  media  (n1, n2, n3):
    return (n1 + n2 + n3) / 3


n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno:'))
n3 = float(input('Terceira nota do aluno:'))

print(f'A média do aluno foi: {media(n1, n2, n3)}')'''

'''print('Questão 2')

def contar_vogais (palavra):
    cont_vogais = 0
    vogais = 'aáàãâeéèêiíìîoóòõôuúùû'
    for letra in palavra.lower():
        if letra in vogais:
            cont_vogais += 1
    return cont_vogais
    

palavra = input('Escreva a palavra:')

print(f'Essa palavra tem {contar_vogais(palavra)} vogais!')'''

'''print('Questão 3 - Primeiro jeito')

def contagem_regressiva (n):
    while n >= 0:
        print(n)
        n -= 1


n = int(input('Insira um número:'))
contagem_regressiva(n)'''

'''print('Questão 3 - Segundo jeito')

def contagem_regressiva (n):
    for i in range(n, -1, -1):
        print(i)


n = int(input('Insira um número:'))
contagem_regressiva(n)'''

'''print('Questão 4')

def maior (a, b):
    if a != b:
        if a > b:
            return a
        return b
    return 'NÚMEROS IGUAIS!'

n1 = float(input('Insira o primeiro número:'))
n2 = float(input('Insira o segundo número:'))

print(f'Maior número:{maior(n1, n2)}')'''

'''print('Questão 5 - Meu jeito')

def media(lista_de_notas):
    soma = 0
    for n in lista_de_notas:
        soma += n
    return soma / len(lista_de_notas)

notas = []
nota = float(input('Escreva a nota ("0" para sair):'))

while nota != 0:
    notas.append(nota)
    nota = float(input('Escreva a nota ("0" para sair):'))

print(f'Média das notas:{media(notas)}')'''

'''print('Questão 5 - Professora jeito')

def media (lista_de_notas):
    return sum(lista_de_notas) / len(lista_de_notas)'''

'''print('Questão 6 - Primeira forma')

def converter_minutos_em_horas (minutos):
    horas = minutos // 60
    minutos = minutos % 60
    return f'{horas} horas e {minutos} minutos'
    

minu = int(input('Insira a quantidade de minutos:'))

print(converter_minutos_em_horas(minu))'''

'''print('Questão 6 - Segunda forma')

def converter_minutos_em_horas (minutos):
    return f'{minutos//60} horas e {minutos%60} minutos'


minu = int(input('Insira a quantidade de minutos:'))

print(converter_minutos_em_horas(minu))'''

'''print('Questão 7 - Primeira forma')

def contar_palavras(frase):
    return len(frase.split(' '))


frase = input('Escreva uma frase:')

print(f'Quantidade de palavras na frase: {contar_palavras(frase)}')'''

'''print('Questão 7 - Segunda forma')

def contar_palavras(frase):
    return frase.count(' ') + 1


frase = input('Escreva uma frase:')

print(f'Quantidade de palavras na frase: {contar_palavras(frase)}')'''
