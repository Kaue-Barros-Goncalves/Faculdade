gabarito = ['e', 'a', 'b', 'c', 'c', 'd', 'e', 'a', 'c', 'd']
resposta = []
cont = 0

while cont < len(gabarito):
    resp = input('Insira a reposta marcada:')
    resposta.append(resp)
    cont += 1

aux = 0
erro = 0
acerto = 0

while aux < len(gabarito):
    if resposta[aux] != gabarito[aux]:
        erro += 1

    else:
        acerto += 1

    aux += 1

if acerto > 5:
    print('Aluno foi aprovado!')

else:
    print('Aluno foi reprovado!')

print('O aluno errou', erro, 'questões!')