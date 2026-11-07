'''print('Questão - 1)a):')

def analisar_clima(temperaturas):
    media = 0
    soma_temp = 0
    for temp in temperaturas:
        if temp >= 15 and temp <= 30:
            soma_temp += temp
            media += 1
    if media != 0:
        return soma_temp / media
    return 0


dados = [12, 18, 25, -5, 32, 20, 14]
print(analisar_clima(dados))'''
    
'''print('Questão - 1)b):')

def balanceamento_estoque(quantidades, meta):
    nova_lista = []
    for quanti in quantidades:
        if quanti < meta:
            quanto_falta = meta - quanti
            nova_lista.append(quanto_falta)
        else:
            nova_lista.append(0)
    return nova_lista


estoque = [10, 50, 35, 5, 60]
objetivo = 40
print(balanceamento_estoque(estoque, objetivo))'''

'''print('Questão - 1)c):')

def formatar_tags(termos, prefixo):
    nova_lista = []
    for palavra in termos:
        if len(palavra) > 3:
            nova_palavra = f'{prefixo}{palavra.upper()}'
            nova_lista.append(nova_palavra)
    return nova_lista


palavras = ['python', 'oi', 'loop', 'ai', 'lista']
print(formatar_tags(palavras, '#'))'''

'''print('Questão - 1)d):')

def atualizar_estoque(estoque, novos_dados):
    for prod, preco, quantidade in novos_dados:
        estoque.update({prod:[preco, quantidade]})
    return estoque


def percorrer_estoque(estoque, novo_estoque):
    total = 0
    for codigo, preco_quanti in estoque.items():
        total = preco_quanti[0] * preco_quanti[1]
        novo_estoque.update({codigo:total})
    return novo_estoque

    
estoque = {'B-0023':[120, 100],
           'C-1570':[600, 40],
           'K-2026':[330, 80]}

dados = [['M-4567', 1500, 10],
         ['D-2346', 1000, 20],
         ['K-2026', 400, 50]]

novo_estoque = {}

print('Estoque atualizado:')
for prod, preco_quanti in atualizar_estoque(estoque, dados).items():
    print(f'Produto: {prod} - Preço: {preco_quanti[0]} - Quantidade: {preco_quanti[1]}')

print(f'{'-' * 50}')

print('Novo estoque:')
for prod, total in percorrer_estoque(estoque, novo_estoque).items():
    print(f'Produto: {prod} - Total acumulado: {total}')'''
