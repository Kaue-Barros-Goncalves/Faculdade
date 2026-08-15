apartamentos = [['101', 320, 290, 310],['102', 180, 200, 175],['103', 410, 390, 420],['104', 260, 240, 280],['105', 150, 160, 145]]
cont = 0

while cont < len(apartamentos):
    consumo_total = apartamentos[cont][1] + apartamentos[cont][2] + apartamentos[cont][3]
    apartamentos[cont].append(consumo_total)
    cont += 1

cont = 0

while cont < len(apartamentos):
    consumo_medio = apartamentos[cont][4] / 3
    apartamentos[cont].append(consumo_medio)
    cont += 1

cont = 0

while cont < len(apartamentos):
    print('Apartamento:', apartamentos[cont][0], '- Consumo total (kWh):', apartamentos[cont][4], '- Consumo médio (kWh):', apartamentos[cont][5])
    cont += 1

cont = 0
aux = 0

while cont < len(apartamentos):
    aux += apartamentos[cont][5]
    cont += 1

consumo_condominio = aux / len(apartamentos)
print('Média geral de consumo do condomínio:', consumo_condominio)

cont = 0

while cont < len(apartamentos):
    if apartamentos[cont][4] > consumo_condominio:
        print('O apartamento',apartamentos[cont][0], 'tem consumo total acima da média geral.')
    cont += 1 