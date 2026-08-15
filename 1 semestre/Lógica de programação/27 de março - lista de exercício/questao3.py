cont = 0
qm = 0 
soma = 0
qh = 0

while cont < 15:
    cont += 1
    idade = int(input('Informe a sua idade:'))
    nac = input('Informe a sua nacionalidade:')
    sexo = input('Informe o seu sexo:')
    
    if sexo == 'mulher' and idade >= 18:
        qm += 1

    if sexo == 'homem' and nac == 'br' and  20 <= idade <= 30:
        qh += 1

    soma += idade

print('A quantidade de mulheres maiores de idade:',qm)
print('A quantidade de homens brasileiros que têm entre 20 e 30 anos:',qh)
print('A média das idades:',soma / 15)