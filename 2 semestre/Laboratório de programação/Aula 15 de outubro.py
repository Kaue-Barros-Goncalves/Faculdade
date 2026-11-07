'''print('Questão 1')
#Crie um dicionário chamado carro com as chaves marca, modelo e ano.
#Depois, imprima apenas o modelo.

carro = {'marca':'Ford', 'modelo':'Ranger Raptor', 'ano':2019,
        'marca':'Fiat', 'modelo':'Siena'}

print(carro['modelo'])'''

'''print('Questão 2')
#Usando o dicionário do exercício anterior, altere o ano para 2024 e
#adicione a chave com valor 'Preto'.

carro = {'marca':'Ford', 'modelo':'Ranger Raptor', 'ano':2019,
        'marca':'Fiat', 'modelo':'Siena'}

carro['ano'] = 2024
carro['cor'] = 'Preto'

print(carro)'''

'''print('Questão 3 - Primeira forma')
#Crie um dicionário com os nomes de 5 países e suas capitais.
#Peça ao Python para exibir apenas os
#nomes dos países (chaves) em formato de lista

paises = {'Brasil':'Brasília', 'França':'Paris', 'Estados Unidos':'Washington',
          'Japão':'Tóquio', 'Alemanha':'Berlim'}

paises_lista = []
capitais_lista = []

for pais in paises.keys():
    paises_lista.append(pais)

for capital in paises.values():
    capitais_lista.append(capital)

print(capitais_lista)
print(paises_lista)'''

'''print('Questão 3 - Segunda forma')

paises = {'Brasil':'Brasília', 'França':'Paris', 'Estados Unidos':'Washington',
          'Japão':'Tóquio', 'Alemanha':'Berlim'}

paises_lista = []
capitais_lista = []

for pais, capital in paises.items():
    paises_lista.append(pais)
    capitais_lista.append(capital)

print(capitais_lista)
print(paises_lista)'''

'''print('Questão 4 - Primeira forma')
# Crie um dicionário de tradução (ex: {"apple": "maçã", "bread": "pão"}).
#Peça para o usuário digitar uma palavra e use o .get() para exibir a tradução
#ou a mensagem "Palavra não encontrada".

traducao = {"apple": "maçã", "bread": "pão", 'cat':'gato', 'table':'mesa'}

palavra = input('Escreva a palavra que queira saber a tradução:').lower()

trad = traducao.get(palavra)

if trad:
    print(f'Tradução de {palavra.capitalize()} para {trad.capitalize()}')

else:
    print('Palavra não encontrada')'''

'''print('Questão 4 - Segunda forma')

traducao = {"apple": "maçã", "bread": "pão", 'cat':'gato', 'table':'mesa'}

palavra = input('Escreva a palavra que queira saber a tradução:').lower()

print(f'Tradução {palavra} para {traducao.get(palavra, 'Palavra não encontrada')}')'''

'''print('Questão 5')
#Crie um dicionário estoque = {"Monitor": 8, "Teclado": 15, "Mouse": 20}.
#Use um loop for com
#.items() para imprimir: "Temos [quantidade] unidades de [produto]".

estoque = {"Monitor": 8, "Teclado": 15, "Mouse": 20}

for produto, quantidade in estoque.items():
    print(f'Temos {quantidade} unidades de {produto}')'''

'''print('Questão 6')
#Dado um dicionário de pessoas e idades:
#pessoas = {"João": 15, "Maria": 22, "Pedro": 17, "Ana": 30}.
#Crie um novo dicionário contendo apenas as pessoas maiores de 18 anos. 

pessoas = {"João": 15, "Maria": 22, "Pedro": 17, "Ana": 30}

maior_18 = {}

for nome, idade in pessoas.items():
    if idade >= 18:
        maior_18.update({nome:idade})

print(f'Pessoas maiores de 18 anos {maior_18}')'''

'''print('Questão 7')
#Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista
#com 3 notas.
#O programa deve calcular a média de cada aluno e imprimir o nome acompanhado
#da média final.

alunos_notas = {
    "Ana": [8.5, 9.0, 7.5],
    "João": [6.0, 5.5, 7.0],
    "Carlos": [9.5, 8.0, 10.0],
    "Maria": [7.0, 8.0, 8.5],
}
for aluno, notas in alunos_notas.items():
    media = sum(notas) / len(notas)
    print(f'O aluno {aluno} obteve a média final {media:.1f}')'''

print('Questão 8')
#Dado um dicionário com os dias da semana e suas respectivas temperaturas:
#clima = {"Seg": 25, "Ter": 30, "Qua": 22, "Qui": 32, "Sex": 28}.
#Crie um código que identifique e imprima qual foi o dia mais quente
#e qual foi a maior temperatura. 

'''clima = {"Seg": 25, "Ter": 30, "Qua": 22, "Qui": 32, "Sex": 28}

dia_quente = ''
maior_temperatura = -999

for dia, temp in clima.items():
    if temp > maior_temperatura:
        dia_quente = dia
        maior_temperatura = temp

print(f'Cidade mais quente: {dia_quente} - Maior temperatura: {maior_temperatura:.1f}°C')'''

'''print('Questão 9')
#Escreva um programa que simule uma votação.
#O usuário deve digitar o nome de um candidato várias vezes em um loop
#(até digitar "sair").
#Use um dicionário para contabilizar os votos.
#Se o nome já existir, some 1. Se não existir, adicione o nome com o valor 1.
#Ao final, mostre o "placar" completo

votacao = {}

candidato = input('Escreva o nome do candidato("sair" para encerrar):').lower().strip()

while candidato != 'sair':
    candidato = candidato.title()

    if candidato in votacao:
        votacao[candidato] += 1

    else:
        votacao[candidato] = 1

    candidato = input('Escreva o nome do candidato("sair" para encerrar):').lower().strip()
    
for candidato, votos in votacao.items():
    print(f'Candidato:{candidato} - Votos:{votos}')

print(f'Total de votos: {sum(votacao.values())}')'''

'''print('Questão 10')
#O usuário informa um "valor limite".
#O programa deve criar um novo dicionário apenas com os itens que custam mais
#que esse valor e, ao final, exibir quantos itens foram filtrados. 

loja = {"Televisão": 2500,
        "Fone": 150,
        "Cadeira": 800,
        "Monitor": 1200,
        "Mouse":90}

nova_loja = {}

valor_limite = int(input('Digite o valor limite:'))

for prod, valor in loja.items():
    if valor > valor_limite:
        nova_loja.update({prod:valor}) #nova_loja[prod] = valor

for prod, valor in nova_loja.items():
    print(f'Produto: {prod} - Valor: {valor}')

print(f'Quantidade de produtos filtrados {len(nova_loja)}')'''
