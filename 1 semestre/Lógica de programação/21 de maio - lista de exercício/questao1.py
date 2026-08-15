listaVasos = [['V01', 100.00, 50.00], ['V02', 80.00, 25.00], ['V03', 110.00, 60.00], ['V04', 230.00, 100.00], ['V05', 25.00, 30.00]]
cont = 0

while cont < len(listaVasos):
    preco_custo = listaVasos[cont][1] + listaVasos[cont][2]
    listaVasos[cont].append(preco_custo)
    cont += 1

cont = 0
vaso = 1

while cont < len(listaVasos):
    print('Código do vaso', vaso, ':', listaVasos[cont][0])
    print('Preço de custo do vaso', vaso, ':', listaVasos[cont][3])
    cont += 1
    vaso += 1

soma = 0
cont = 0

while cont < len(listaVasos):
    soma += listaVasos[cont][3]
    cont += 1

media = soma / len(listaVasos)

print('Média dos preços de custo dos vasos:', media)

cont = 0

while cont < len(listaVasos):
    if listaVasos[cont][3] < media:
        print('O vaso', listaVasos[cont][0], 'tem o preço de custo menor que a média calculada!')

    cont += 1