cont = 0
sm = float(input('Valor do salário mínimo (em R$):'))
vr = 0
maiorsalario = 0

while cont < 30:
    cont += 1
    nome = input('Informe o seu nome:')
    setor = input('Qual o setor (r - roupas ou c - calçados):')
    vtv = float(input('Valor total das vendas efetuadas no mês:'))
    salario = sm + (vtv *0.08)
    print(nome,'- R$',salario)

    if setor == 'r':
        vr += 1

    if setor == 'c':
        
        if salario > maiorsalario:
            maiorsalario = salario

print('Percentual de vendedores de roupas:',(vr / 30) * 100)
print('O maior salário do setor de calçados:',maiorsalario)