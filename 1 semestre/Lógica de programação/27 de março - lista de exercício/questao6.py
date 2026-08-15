cont = 0
menorimc = 999

while cont < 10:
    cont += 1
    nome = input('Informe o seu nome:')
    peso = float(input('Informe o seu peso:'))
    altura = float(input('Informe a sua altura:'))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(nome,'- Abaixo do Peso')

    elif 18.5 < imc <= 25:
        print(nome,'- Peso Normal')

    elif 25 < imc <= 30:
        print(nome,'- Acima do Peso')

    elif 30 < imc:
        print(nome,'- obesidade')

    if imc < menorimc:
        menorimc = imc

print('O menor imc é:',menorimc)