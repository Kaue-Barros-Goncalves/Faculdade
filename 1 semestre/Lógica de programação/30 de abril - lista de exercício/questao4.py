cont = 0
lista_media = []
media_geral = 0
quantidade_maior = 0

while cont < 5:
    nota1 = float(input('Primeira nota do aluno:'))
    nota2 = float(input('Segunda nota do aluno:'))

    media = (nota1 + nota2) / 2

    lista_media.append(media)

    media_geral += media

    cont += 1

media_geral = media_geral / len(lista_media)
print('Média geral da turma:',media_geral)

cont = 0

while cont <  len(lista_media):

    if lista_media[cont] > media_geral:
        quantidade_maior += 1

    cont += 1

print('Quantidade de alunos com média maior que a média da turma:', quantidade_maior)