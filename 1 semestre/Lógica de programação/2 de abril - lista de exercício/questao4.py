criancas_nascidas = int(input('Informe quantas crianças nasceram no período:'))
porcentagem_crianca_morta = 0
nao_1ano = 0
masculino_1ano = 0
sexo = input("Digite o sexo da próxima criança (ou inválido para sair):")

while sexo == 'masculino' or sexo == 'feminino':

    tempo_vida = int(input('Informe quantidade de meses de vida da criança:'))

    if tempo_vida < 12:
        nao_1ano += 1

    if sexo == 'masculino' and tempo_vida >= 12:
        masculino_1ano += 1

    porcentagem_crianca_morta += 1

    sexo = input("Digite o sexo da próxima criança (ou inválido para sair):")

print('Porcentagem das crianças mortas no período:',(porcentagem_crianca_morta / criancas_nascidas) * 100)
print('Quantidade de crianças que não chegaram a completar 1 ano de vida:',nao_1ano)
print('Quantidade de crianças do sexo masculino mortas no período que viveu ano ou mais:',masculino_1ano) 