registro = []

while continuar != 'não':
    nome_livro = input('Título do livro ("sair" para encerrar):')
    aluno = input('Nome do aluno:')
    dias = int(input('Quantidade de dias que ficou emprestado:'))
    
    registro.append([nome_livro, aluno, dias])

    continuar = input('Deseja continuar? (sim ou não):')

cont = 0

while cont < len(registro):
    print(registro[cont])
    cont += 1

quantidade_multas = 0
cont = 0

while cont < len(registro):
    if registro[cont][2] > 14:
        multa = (registro[cont][2] - 14) * 0.50
        registro[cont].append(multa)
        quantidade_multas += 1
    cont += 1

cont = 0
mais_tempo = registro[0][2]
nome_mais_tempo = ''

while cont < len(registro):
    if registro[cont][2] > mais_tempo:
        nome_mais_tempo = registro[cont][0]
    cont += 1

print('Livro que ficou mais tempo emprestado:', nome_mais_tempo)
print('Quantidade de empréstimos que geraram multas', quantidade_multas)