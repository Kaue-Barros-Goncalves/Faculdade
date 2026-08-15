flores = []
continuar = 's'

while continuar == 's':
    flor = []
    flor.append(input("Digite o nome da flor: "))
    flor.append(float(input("Digite o preço da unidade da flor:"))) 
    flores.append(flor)

    continuar = input("Deseja continuar a inserção? (S/N): ")
    
print(flores)
print("\nFlores cadastradas")

i = 0

while i < len(flores):
    print("Flor ", i) 
    print("Nome: ", flores[i][0])
    print("Preço da unidade: R$ ", flores[i][1])
    i = i + 1
print("\nRelatório Final")

i = 0

while i < len(flores):
    valor_buque = flores[i][1] * 12
    print(i, "-", flores[i][0], "- Valor do buquê: R$",valor_buque)
    i = i + 1

maior_preco = 0
i = 0

while i < len(flores):
    if flores[i][1] > maior_preco:
        maior_preco = flores[i][1]
    i = i + 1

print("\nFlor(es) mais cara(s):") 

i = 0

while i < len(flores):
    if flores[i][1] == maior_preco:
        print("Nome: ", flores[i][0], "Valor: R$", flores[i][0])
    i = i + 1
