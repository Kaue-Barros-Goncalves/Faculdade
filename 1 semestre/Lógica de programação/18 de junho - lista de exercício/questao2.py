cidades = []
cont = 0

while cont < 7:
    nome = input('Nome da cidade:')
    temp1 = float(input('Temperatura dia 1:'))
    temp2 = float(input('Temperatura dia 2:'))
    temp3 = float(input('Temperatura dia 3:'))
    cidades.append([nome, temp1, temp2, temp3])
    cont += 1

cont = 0

while cont < len(cidades):
    media = (cidades[cont][1] + cidades[cont][2] + cidades[cont][3]) / 3
    cidades[cont].append(media)
    print('a cidade', cidades[cont][0], 'teve uma temperatuda média de', cidades[cont][4], '°C.')
    cont += 1

cont = 0
maior_media = cidades[0][4]
menor_media = cidades[0][4]

while cont < len(cidades):
    if cidades[cont][4] > maior_media:
        maior_media = cidades[cont][4]

    if cidades[cont][4] < menor_media:
        menor_media = cidades[cont][4]
    cont += 1

cont = 0

while cont < len(cidades):
    if cidades[cont][4] == maior_media:
        print('Cidade com a maior média de temperatura:', cidades[cont][0])
    cont += 1

cont = 0

while cont < len(cidades):
    if cidades[cont][4] == menor_media:
        print('Cidade com a menor média de temperatura:', cidades[cont][0])
    cont += 1