cinto = input('Está usando o cinto de segurança? ‘s’ (para sim) ou ‘n’ (para não):').lower()
sobrio = input('Está sóbrio para dirigir? ‘s’ (para sim) ou ‘n’ (para não):').lower()
carro = input('O carro está com a revisão em dia? ‘s’ (para sim) ou ‘n’ (para não):').lower()

if cinto == 's' and sobrio == 's' and carro == 's':
    print('O motorista está com condição de dirigir com segurança.')

else:
    print('O motorista não está em condições de dirigir com segurança.')