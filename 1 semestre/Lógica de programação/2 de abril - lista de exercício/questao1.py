funcionario = ''
media = 0
cont = 0
salario_mais_baixo = float('inf')
salario_mais_alto = float('-inf')
nome_baixo = ''
nome_alto = ''
funcionario = input('Nome do funcionário (para encerrar digite "fim"):')

while funcionario != 'fim':
    salario = float(input('Informe o seu salário: R$'))
    media += salario
    cont += 1

    if salario > salario_mais_alto:
        salario_mais_alto = salario
        nome_alto = funcionario

    if salario < salario_mais_baixo:
        salario_mais_baixo = salario
        nome_baixo = funcionario

    funcionario = input('Nome do funcionário (para encerrar digite "fim"):')

print('Média dos salário:',media / cont)
print('Salário mais alto:',nome_alto,'-',salario_mais_alto)
print('Salário mais baixo:',nome_baixo,'-',salario_mais_baixo)