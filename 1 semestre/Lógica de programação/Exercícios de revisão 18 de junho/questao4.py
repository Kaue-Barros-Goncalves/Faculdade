vendas = [200, 450, 700, 100, 300]
cont = 0
maior = -99999999
menor = 99999999
total = 0

while cont < len(vendas):
    if vendas[cont] > maior:
        maior = vendas[cont]

    if vendas[cont] < menor:
        menor = vendas[cont]

    total += vendas[cont]
    cont += 1

print('Maior valor vendido:', maior)
print('Menor valor vendido:', menor)
print('Total vendido:', total)