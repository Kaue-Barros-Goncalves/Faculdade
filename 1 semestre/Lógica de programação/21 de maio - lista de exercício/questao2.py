participantes = []
cont = 0

while cont < 50:
    nome = input('Insira o nome do participante:')
    setor = input('Insira o setor do participante:')
    escrita = float(input('Insira a nota da prova escrita do participante:'))
    pratica = float(input('Insira a nota da prova prática do participante:'))
    
    participantes.append([nome, setor, escrita, pratica])
    cont += 1

cont = 0

while cont < len(participantes):
    print(participantes[cont])
    cont += 1

cont = 0

while cont < len(participantes):
    soma = participantes[cont][2] + participantes[cont][3]

    if soma >= 7:
        print('O participante', participantes[cont][0], 'foi aprovado!')

    cont += 1

cont = 0
setor2 = input('Insira um setor para saber:')

while cont < len(participantes):

    if setor2 == participantes[cont][1]:
        print('Nome do participante do mesmo setor:', participantes[cont][0])

    cont += 1