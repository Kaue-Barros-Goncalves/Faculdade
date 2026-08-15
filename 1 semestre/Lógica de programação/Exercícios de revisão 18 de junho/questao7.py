nomes = []
cont = 0

while cont < 4:
    n = input('Informe os nomes:')
    nomes.append(n)
    cont += 1

cont = 0

while cont < len(nomes):
    nome_acesso = input('Informe o nome para saber se tem acesso ou não:')