preco = float(input('Preço do ingresso: '))
profissao = input('Sua profissão (estudante/professor/bombeiro/artista profissional): ')
idade = int(input('Informe sua idade: '))

cal = preco

if profissao == 'estudante' or profissao == 'professor':
    cal = cal / 2
elif profissao == 'bombeiro':
    cal = cal - 15
elif profissao == 'artista profissional':
    cal = cal - 10
else:
    print('Sua profissão não tem desconto.')

if idade >= 60 or idade <= 10:
    cal = cal - 20

if cal < 0:
    cal = 0

print( 'O preço do seu ingresso é: R$',cal)