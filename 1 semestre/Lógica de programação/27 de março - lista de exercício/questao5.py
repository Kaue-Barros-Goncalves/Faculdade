cont = 0 
vb = 0
vt = 0
vr = 0
total = 0

while cont < 50:
    cont += 1
    tv = input('Tipo de vinho (B - Branco, T - Tinto e R - Rosé):')

    if tv == 'B':
        vb += 1

    elif tv == 'T':
        vt += 1

    elif tv == 'R':
        vr += 1

    else:
        print("Entrada inválida! Digite apenas B, T ou R.")

print('Percentual de vinho branco:',(vb / 50) * 100)
print('Percentual de vinho tinto:',(vt / 50) * 100)
print('Percentual de vinho rosé:',(vr / 50) * 100)