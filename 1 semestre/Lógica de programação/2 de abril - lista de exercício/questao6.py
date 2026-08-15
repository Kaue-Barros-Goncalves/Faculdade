casas_canal4 = 0
pessoas_canal5 = 0
numero_canal = int(input('Informe o número do canal (4 ou 5) (para encerrar digite 0):'))

while numero_canal != 0:

    pessoas = int(input('Informe a quantidade de pessoas que assistem na casa:'))

    if numero_canal == 4:
        casas_canal4 += 1

    elif numero_canal == 5:
        pessoas_canal5 += pessoas

    numero_canal = int(input('Informe o número do canal (4 ou 5) (para encerrar digite 0):'))

print('Quantidade de casas que assistem o canal 4:',casas_canal4)
print('Quantidade de pessoas que assistem o canal 5:',pessoas_canal5)