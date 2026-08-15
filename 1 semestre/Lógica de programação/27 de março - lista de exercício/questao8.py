cont = 0
maiornota = 0
result = 0
questoes= int(input('Informe quanats questões a prova tinha:'))

while cont < 5:
    cont += 1
    nome = input('Informe o seu nome:')
    acertos = int(input('Informe a quantidade questões acertadas:'))
    print('Nota do',nome,':',acertos)
    result += acertos
    
    if acertos > maiornota:
        maiornota = acertos

print('Média das notas dos candidatos:',result / cont)
print('Maior nota entre os candidatos:',maiornota)