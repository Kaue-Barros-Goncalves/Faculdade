vendas = {'bonés':30, 'camisas':50, 'blusas':60}

#.get()

'''print(vendas.get('camisas', 'Não existe esse item'))

print(vendas.get('calças', 'Não existe esse item'))

print(vendas.get('bolsas', 150))'''

#Manipulando dicionário

'''vendas['calças'] = 100

vendas['bonés'] = 250

print(vendas)'''

#Somando as chaves

'''nums = {'a':20, 'b':30, 'c':50}

soma = 0
for chave in nums:
    soma += nums[chave]

print(soma)'''

#.values()

'''nums = {'a':20, 'b':30, 'c':50}

soma = 0
for valor in nums.values():
    soma += valor

print(soma)'''

#Dicionários dentro de lista

'''alunos = [{'Nome':'Maria', 'MAT':'0001'},
          {'Nome':'Joaquim','MAT':'0020'},
          {'Nome':'Ana','MAT':'0032'}]

for aluno in alunos:
    print(f'{aluno['Nome']} - {aluno['MAT']}')'''
