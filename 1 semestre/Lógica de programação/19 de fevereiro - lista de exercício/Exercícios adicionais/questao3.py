import random
valorAleatorio = random.randint(1, 10)
n1 = float(input('Escreva o seu número:'))

if n1 < valorAleatorio:
    print('Seu número é menor q o valor gerado aleatoriamente.')

elif n1 > valorAleatorio:
    print('Seu número é maior q o valor gerado aleatoriamente.')

else:
    print('Seu número é igual ao valor gerado aleatoriamente.')