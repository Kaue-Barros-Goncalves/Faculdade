#Arquivo em formato .txt
#'r' - read()
#'w' - write()
#'a' - append()
#'x' - cria um novo arquivo

'''arquivo = open('teste1.txt', 'a')

arquivo.write('Maçã\n')

arquivo.write('Amora\n')

arquivo.close()'''

#Para não precisar escrever o .close()

'''with open('teste2.txt', 'w', encoding='utf-8') as arq1:
    arq1.write('João\n')
    arq1.write('Maria\n')
    arq1.write('José\n')'''

#Ler o arquivo
#.read() - retorna todo o conteúdo
#.readline() - retorna a uma linha
#.readlines() - retorna uma lista

'''with open('teste2.txt', 'r', encoding = 'utf-8') as arquivo:
    read = arquivo.read()
    readline = arquivo.readline()
    readlines = arquivo.readlines()
    print(read)
    print(readline)
    print(readlines)'''

#Usando o for

'''with open('teste2.txt', 'r', encoding = 'utf-8') as arquivo:
    for linha in arquivo.readlines():
        print(linha.strip())'''

#Atividade

'''print('Questão 1 - primeira forma')

with open('vendas.txt', 'w', encoding = 'utf-8') as arq:
    arq.write('P200;bonés;100;25.5\n')
    arq.write('B021;blusas;150;100.0\n')
    arq.write('C237;chápeu;50;50.0\n')

with open('vendas.txt', 'r', encoding = 'utf-8') as arq:
    for linha in arq.readlines():
        dados = linha.strip().split(';')
        cod = dados[0]
        prod = dados[1]
        qtde = dados[2]
        preco = float(dados[3])
        
        print(f'{prod.capitalize()}({cod}) - {qtde} unidades - R${preco:.2f}')'''
        
'''print('Questão 1 - segunda forma')

with open('vendas.txt', 'w', encoding = 'utf-8') as arq:
    arq.write('P200;bonés;100;25.5\n')
    arq.write('B021;blusas;150;100.0\n')
    arq.write('C237;chápeu;50;50.0\n')

with open('vendas.txt', 'r', encoding = 'utf-8') as arq:
    for linha in arq.readlines():
        cod, prod, qtde, preco = linha.strip().split(';')
        preco = float(preco)

        with open('relatorio.txt', 'a', encoding = 'utf-8') as arq1:
            arq1.write(f'{prod.capitalize()}({cod}) - {qtde} unidades - R${preco:.2f}\n')'''

'''print('Questão 1 - terceira forma')

with open('vendas.txt', 'w', encoding = 'utf-8') as arq:
    arq.write('P200;bonés;100;25.5\n')
    arq.write('B021;blusas;150;100.0\n')
    arq.write('C237;chápeu;50;50.0\n')

with open('vendas.txt', 'r', encoding = 'utf-8') as arq:
    dados = []
    for linha in arq.readlines():
        cod, prod, qtde, preco = linha.strip().split(';')
        preco = float(preco)
        dados.append(f'{prod.capitalize()}({cod}) - {qtde} unidades - R${preco:.2f}\n')
    
with open('relatorio.txt', 'a', encoding = 'utf-8') as arq1:
    for linha in dados:
        arq1.write(linha)'''

print('Questão 2')

def adicinar_aluno(cod, nome, n1, n2, n3):
    while True:
        cod = input('Código do aluno:').upper()
        if cod[:2].isalpha() and cod[2:].isnumeric():
            break
        else:
            print('Código inválido')
    nome = input('Nome do aluno:')
    n1 = float(input('Primeira nota do aluno:'))
    n2 = float(input('Segunda nota do aluno:'))
    n3 = float(input('Terceira nota do aluno:'))


with open('alunos.txt', 'w', encoding = 'utf-8') as arq:
    arq.write('ES202,Ana,9.0,8.5,7.0\n')
    arq.write('ES587,João,6.0,5.0,7.0\n')
    arq.write('ES074,Maria,5.0,4.0,3.0\n')

with open('alunos.txt', 'r', encoding = 'utf-8') as arq:
    for linha in arq.readlines():
        cod, nome, n1, n2, n3 = linha.strip().split(',')
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        media = (n1 + n2 + n3) / 3
        
        with open('medias.txt', 'a', encoding = 'utf-8') as arq1:
            arq1.write(f'{cod} - {media:.1f}\n')

        with open('aprovacoes.txt', 'a', encoding = 'utf-8') as arq2:
            if media >= 6.0:
                arq2.write(f'{nome.capitalize()} - aprovado(a)\n')
            else:
                arq2.write(f'{nome.capitalize()} - reprovado(a)\n')
