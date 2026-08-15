calculo = input('Escolha a opção: “so” - soma, “su” - subtração, “pr” - produto ou “di” – divisão:')

if calculo != 'so' and calculo != 'su' and calculo != 'pr' and calculo != 'di':
    print('Opção inválida!')

else:
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))

    if calculo == 'so':
        soma = n1 + n2
        print('Resultado:', soma)
    
    elif calculo == 'su':
        
        if n1 < n2:
            sub = n2 - n1
            print('Resultado:', sub)

        else:
            sub = n1 - n2
            print('Resultado:', sub)

    elif calculo == 'pr':
        multi = n1 * n2
        print('Resultado:', multi)

    elif n2 == 0:
        print('Não pode ser feita a divisão por 0!')

    else:
        divi = n1 / n2
        print('Resultado:', divi)