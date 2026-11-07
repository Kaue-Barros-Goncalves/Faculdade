import bib_kaue as bk

while True:
    bk.imprimir(10)
    print('1 - Somar\n'
          '2 - Dividir\n'
          '3 - Raíz quadrada\n'
          '4 - Seno\n'
          '0 - Sair')

    opcao = input('Digite a opção:')
    if opcao == '0':
        break
    elif opcao == '1':
        print('Soma de 2 números')
        print('Soma:', bk.somar())
        
    elif opcao == '2':
        print('Divisão de 2 números')
        print('Divisão:', bk.dividir())
        
    elif opcao == '3':
        print('Raíz quadrada')
        print('Raíz:', bk.raiz_quadrada())
        
    elif opcao == '4':
        print('Seno de um ângulo')
        print('Seno:', bk.seno())
