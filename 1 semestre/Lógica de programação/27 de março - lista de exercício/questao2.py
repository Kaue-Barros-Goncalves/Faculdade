cont = 0
media = 0
ql = 0

while cont < 5:
    cont = cont + 1
    media = media + 1
    pc = float(input('Preço de compra:'))
    pv = float(input('Preço de venda:'))
    lucro = pv - pc
    ql += lucro
    print('Lucro da escultura:',lucro)

print('Média dos lucros:',ql / media)