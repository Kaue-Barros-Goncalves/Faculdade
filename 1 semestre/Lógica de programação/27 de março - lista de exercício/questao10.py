cont = 0
maior_idade = 0
nome_velho = ''

while cont < 2:
    cont += 1   
    nome = input('Informe o seu nome:')
    idade = int(input('Informe a sua idade:'))

    if idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

print('Pessoa mais velha é:',nome,'-',maior_idade)