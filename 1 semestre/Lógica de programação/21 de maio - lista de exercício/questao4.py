bolos = [['Laranja', 10, 8, 15.00], ['Chocolate', 20, 17, 12.00], ['Banana', 15, 10, 13.00], ['Fubá', 20, 17, 15.00], ['Milho', 15, 14, 13.00]]
cont = 0

while cont < len(bolos):
    sobra = bolos[cont][1] - bolos[cont][2]
    bolos[cont].append(sobra)
    cont += 1

cont = 0

while cont < len(bolos):
    lucro_total = bolos[cont][2] * bolos[cont][3]
    bolos[cont].append(lucro_total)
    cont += 1

maior_quantidade = 0
cont = 0

while cont < len(bolos):
    if bolos[cont][2] > maior_quantidade:
        maior_quantidade = bolos[cont][2]
    cont += 1

print('Maior quantidade vendida:', maior_quantidade)
cont = 0

while cont < len(bolos):
    if bolos[cont][2] >= maior_quantidade:
        print('Bolo que vendeu uma quantidade igual a maior quantidade vendida:', bolos[cont][0])
    cont += 1