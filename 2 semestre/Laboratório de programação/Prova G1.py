'''print('Questão 1')

hospedes = [['RES-7788', 'carlos eduardo lima', 'são paulo'],
            ['RSV-4321', 'beatriz souza alves', 'rio de janeiro'],
            ['HOT-9911', 'FERNANDA LIMA COSTA', 'belo horizonte']]

cartoes_acesso = []
for codigo, nome, cidade in hospedes:
    numeros_codigo = f'{codigo[-3:]}_'
    nome_formatacao = nome.split(' ')
    primeiro_nome = f'{nome_formatacao[0].lower().capitalize()}_'
    cidade_formatacao = cidade.replace(' ', '').upper()
    letras_cidade = cidade_formatacao[:5]
    novo_acesso = f'{numeros_codigo}{primeiro_nome}{letras_cidade}'
    cartoes_acesso.append([novo_acesso])

cartoes_acesso.sort(reverse=True)

for i in cartoes_acesso:
    print(i)'''

'''print('Questão 2')

consumo = ['CafeExpresso: 12.0',
           'PaoDeQueijo: 6.5',
           'BoloChocolate: 15.0']

for produto in consumo:
    produto_valor = produto.split(':')
    gorjeta = float(produto_valor[1]) * (15 / 100)
    taxa = float(produto_valor[1]) + gorjeta
    nome_produto = produto_valor[0].upper()
    print(f'Item: {nome_produto} | Total com taxa (15%): {taxa:.2f}')'''

'''print('Questão 3')

inventario = [['Notebook Dell', 'Recursos Humanos', 2021],
              ['servidor rack', 'infraestrutura', 2019],
              ['IMPRESSORA LASER', 'financeiro', 2023]]

equipamentos = []
setores = []
i = True
while i == True:
    print(f'{'-' * 30}INVENTÁRIO{'-' * 30}')
    print('0 - Sair')
    print('1 - Equipamentos antes de determinado ano')
    print('2 - Verificar setor')
    print('3 - Dados do inventário')
    numero = int(input('Escreva o número:'))

    if numero == 1:
        ano = int(input('Informe qual o ano:'))
        for produto, setor, ano_aquisicao in inventario:
            equipamento = produto.upper()
            if ano > ano_aquisicao:
                 equipamentos.append([equipamento, ano_aquisicao])

        for equipamento, ano_aquisicao in equipamentos:
            print(f'Equipamento:{equipamento} | Ano de aquisição:{ano_aquisicao}')

    elif numero == 2:
        for produto, setor, ano_aquisicao in inventario:
            setores.append(setor.upper())

        setor = input('Qual o setor:').upper()

        if setor in setores:
            print(f'Há equipamentos cadastrados no setor:{setor}')
        else:
            print(f'Não há equipamentos cadastrados nesse setor:{setor}')

    elif numero == 3:
        for produto, setor, ano_aquisicao in inventario:
            print(f'Equipamento: {produto.lower().capitalize()} - Setor: {setor.upper()}')

    elif numero == 0:
        i = False'''
