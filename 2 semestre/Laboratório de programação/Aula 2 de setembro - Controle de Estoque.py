import copy

estoque = [["Teclado", 15],
           ["Mouse", 40],
           ["Monitor", 8],
           ["Webcam", 12],
           ["Headset", 25],
           ["Mousepad", 50],
           ["Cabo HDMI", 30]]

estoque_original = copy.deepcopy(estoque)

opcao = -1

while opcao != 0:
    print("\n" + "=" * 50)
    print("       SISTEMA DE CONTROLE DE ESTOQUE")
    print("=" * 50)
    print("1 - Consultar estoque atual")
    print("2 - Consultar estoque inicial")
    print("3 - Cadastrar novo prouto")
    print("4 - Inserir produto em posição específica")
    print("5 - Atualizar quantidade de um produto")
    print("6 - Remover produto")
    print("7 - Retirar último item do estoque")
    print("8 - Localizar produto e sua posição")
    print("9 - Exibir indicadores do estoque")
    print("10 - Listar produtos com estoque crítico")
    print("0 - Encerrar sistema")
    print("=" * 50)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n ESTOQUE ATUAL ")
        for i, (prod, qtd) in enumerate(estoque):
            print(f"{i + 1} - {prod} -> Quantidade: {qtd}")

    elif opcao == 2:
        print("\n  ESTOQUE INICIAL ")
        for i, (prod, qtd) in enumerate(estoque_original):
            print(f"{i + 1} - {prod} -> Quantidade: {qtd}")

    elif opcao == 3:
        print("\n CADASTRAR NOVO PRODUTO ")
        produto = input("Insira o nome do produto:")
        quantidade = int(input("Insira a quantidade do produto:"))
        estoque.append([produto, quantidade])

    elif opcao == 4:
        print("\n INSERIR PRODUTO EM POSIÇÃO ESPECÍFICA ")
        produto = input("Insira o nome do produto:")
        quantidade = int(input("Insira a quantidade do produto:"))
        posicao = int(input("Insira a posição desejada:"))
        estoque.insert(posicao - 1, [protudo, quantidade])
        
    elif opcao == 5:
        print("\n ATUALIZAR A QUANTIDADE DE UM PRODUTO ")
        achou = False
        produto = input("Insira o produto que queira atualizar o estoque:")
        for item in estoque:
            if produto == item[0]:
                item[1] = int(input("Insira a nova quantidade:"))
                achou = True
        if not achou:
            print("Não existe esse produto dentro da lista")

    elif opcao == 6:
        print("\n REMOVER PRODUTO ")
        achou = False
        produto = input("Insira o produto que queira remover no estoque:")
        for item in estoque:
            if produto == item[0]:
                estoque.remove(item)
                achou = True

        if not achou:
            print("Não existe esse produto dentro da lista")
            
    elif opcao == 7:
        print("\n RETIRAR ÚLTIMO ITEM DO ESTOQUE ")
        removido = estoque.pop()
        print(f"Produto removido: {removido[0]} - {removido[1]}")

    elif opcao == 8:
        print("\n LOCALIZAR PRODUTO E SUA POSIÇÃO ")
        achou = False
        produto = input("Insira o nome do produto que queira localizar:")
        for item in estoque:
            if produto == item[0]:
                posicao = estoque.index(item)
                print(f"O produto está na posição: {posicao + 1}")
                print(f"Quantidade desse produto: {item[1]}")
                achou = True
        if not achou:
            print("Não existe esse produto na lista")

    elif opcao == 9:
        print("\n LOCALIZAR INDICADORES DO ESTOQUE ")
        print(f"Total de produtos cadastrados: {len(estoque)}")
        quantidades = []
        for _, qtde in estoque:
            quantidades.append(qtde)
        print(f"Menor estoque encontrado: {min(quantidades)}")
        print(f"Maior estoque encontrado: {max(quantidades)}")
        print(f"Quantidade total de itens no armazém: {sum(quantidades)}")
        print(f"Quantidade média por produto: {sum(quantidades) / len(estoque):.2f}")

    elif opcao == 10:
        soma = 0
        for item in estoque:
            soma += item[1]
        media = soma / len(estoque)
        print("Produtos em estoque crítico:")
        for item in estoque:
            if item[1] < media:
                print(item[0])
