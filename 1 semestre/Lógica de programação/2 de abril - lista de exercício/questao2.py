escultura_mais_cara = float('-inf')
nome_caro = ''
cat_barata = ''
preco_barato = float('inf')
preco = float(input('Informe o preço da obra (para encerrar digite "0"):'))

while preco != '0':

    nome = input('Nome do artista:')
    cat = input('Categoria da obra (escultura ou quadro):')

    if cat == 'escultura' and preco > escultura_mais_cara:
        escultura_mais_cara = preco
        nome_caro = nome

    if preco < preco_barato:
        preco_barato = preco
        cat_barata = cat

    preco = float(input('Informe o preço da obra (para encerrar digite "0"):'))

print('Nome do artista que tem a escultura mais cara:',nome_caro)
print('Categoria da obra mais barata:',cat_barata,'-',preco_barato) 