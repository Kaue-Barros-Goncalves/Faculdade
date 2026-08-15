jogadores = []
cont = 0

while cont < 10:
    nome = input('Nome do jogador:')
    vit = int(input('Número de vitórias:'))
    der = int(input('Número de derrotas:'))
    emp = int(input('Número de empates:'))
    jogadores.append([nome, vit, der, emp])
    cont += 1

cont = 0

while cont < len(jogadores):
    pontuacao_total = (jogadores[cont][1] * 3) + jogadores[cont][3]
    jogadores[cont].append(pontuacao_total)
    print('O jogador', jogadores[cont][0], 'tem', pontuacao_total, 'pontos!')
    cont += 1

maior_pontuacao = 0
cont = 0

while cont < len(jogadores):
    if jogadores[cont][4] > maior_pontuacao:
        maior_pontuacao = jogadores[cont][4]
    cont += 1

print('Maior pontuação do torneio:', maior_pontuacao)

nome = []
cont = 0

while cont < len(jogadores):
    if jogadores[cont][4] == maior_pontuacao:
        nome.append(jogadores[cont][0])
    cont += 1

print('Jogadores que atingiram a pontuação máxima:', nome)