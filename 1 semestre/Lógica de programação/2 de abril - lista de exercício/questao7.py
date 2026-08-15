ano = int(input('informe o ano atual:'))
populacao = float(input('Informe a população da cidade:'))

print(ano,'-',populacao)

while ano < 2050:
    ano += 1
    populacao = populacao * 1.10

    print(ano,'-',populacao)