vi = input('Seu animal é vertebrado ou invertebrado?:')
especie = input('Seu animal é de qual espécie?:')
alimento = input('Qual o tipo de alimentação do seu animal?:')

if vi == 'vertebrado':

    if especie == 'ave':

        if alimento == 'carnivoro':
            print('Seu animal é (águia).')

        elif alimento == 'onivoro':
            print('Seu animal é (pombo).')

    elif especie == 'mamifero':

        if alimento == 'onivoro':
            print('Seu animal é (homem).')

        elif alimento == 'herbivoro':
            print('Seu animal é (vaca).')

elif vi == 'invertebrado':

    if especie == 'inseto':

        if alimento == 'hematofago':
            print('Seu animal é (pulga).')

        elif alimento ==  'herbivoro':
            print('Seu animal é (lagartixa).')

    elif especie == 'anelideo':

        if alimento == 'hematofago':
            print('Seu animal é (sanguessuga).')

        elif alimento == 'onivoro':
            print('Seu animal é (minhoca).')