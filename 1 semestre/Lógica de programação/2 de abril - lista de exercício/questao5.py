num = float(input('Informe o seu número:'))
divisoes = 0

while num >= 1:
    num = num / 2
    divisoes += 1

print('Resultado da última deivisão:',num)
print('Quantidade de divisões:',divisoes)