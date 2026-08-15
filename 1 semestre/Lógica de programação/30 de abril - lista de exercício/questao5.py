lista = []
palavra = input('Informe a sua palavra ("sair" para encerrar):')

while palavra != 'sair':
    lista.append(palavra)

    palavra = input('Informe a sua palavra ("sair" para encerrar):')

cont = 0
verificar = input('Escreva a palavra:')

while cont < len(lista):
    if verificar in lista[cont]:
        lista[cont] = 'ELIMINADA'

    else:
        print('Não existe na lista.')

    cont += 1