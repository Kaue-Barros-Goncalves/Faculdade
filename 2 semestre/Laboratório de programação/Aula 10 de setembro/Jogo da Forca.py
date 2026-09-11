palavra_secreta = input('Digite a palavra secreta:').upper()
erros = []
adivinhacoes = []

for letra in palavra_secreta:
    adivinhacoes.append('_')

chances = 5
    
print(' '.join(adivinhacoes))

while '_' in adivinhacoes and chances > 0:
    print(f'Letras erradas: {', '.join(erros)}')
    print(f'Você têm {chances} chances'.upper())
    chute = input('Digite uma letra:').upper()
    
    for i, letra in enumerate(palavra_secreta):
        if letra == chute:
                adivinhacoes[i] = chute
        
    if chute in palavra_secreta:
        print('Você acertou!')
        print(f'Elementos assim: {' '.join(adivinhacoes)}')

    else:
        print('Você errou!')
        print(f'Elementos assim: {' '.join(adivinhacoes)}')
        erros.append(chute)
        chances -= 1
        
    print('-' * 50)

if '_' in adivinhacoes:
    print('Você perdeu!'.upper())

else:
    print('Você ganhou!'.upper())
