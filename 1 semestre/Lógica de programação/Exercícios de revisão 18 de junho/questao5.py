notas = []
soma = 0
n = float(input('Insira a nota (negativo para encerrar):'))

while n >= 0:
    notas.append(n)
    soma += n
    n = float(input('Insira a nota (negativo para encerrar):'))

media = soma / len(notas)
print('Notas:', notas)
print('Média das notas:', media)