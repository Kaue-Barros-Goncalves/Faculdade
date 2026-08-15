#Exemplo 1a (while):

'''soma = 0
1 = 1
while i < 101:
    soma += 1
    1 += 1

print(soma)'''

#Exemplo 1b (for):

'''soma = 0
for i in range(101):
    soma += i


print(soma)'''

#Questão 1 - Imprimir os números pares de 20 a 0 (for):

'''for i in range(20,-1,-1):
    if i % 2 == 0:
        print(i)'''

#Questão 2 - Falar qual aluno foi reprovado (for):

#Método 1:

'''alunos = [['Ana', 7.5], ['Maria', 8.0], ['João', 5.0], ['José', 4.5]]
for i in range(len(alunos)):
    if alunos[i][1] >= 6.0:
        print(f'{alunos[i][0]}:aprovado(a)')
    else:
        print(f'{alunos[i][0]}:reprovado(a)')'''

#Método 2:

'''alunos = [['Ana', 7.5], ['Maria', 8.0], ['João', 5.0], ['José', 4.5]]
for aluno in alunos:
    if aluno[1] >= 6.0:
        print(f'{aluno[0]}:aprovado(a)')
    else:
        print(f'{aluno[0]}:reprovado(a)')'''

#Método 3:

'''alunos = [['Ana', 7.5], ['Maria', 8.0], ['João', 5.0], ['José', 4.5]]
for nome,nota in alunos:
    if nota >= 6.0:
        print(f'{nome}:aprovado(a)')
    else:
        print(f'{nome}:reprovado(a)')'''

#Questão 3 - Falar a média de cada aluno (for):

'''alunos = [['Ana', 7.5, 8.0, 8.5],
          ['Maria', 8.0, 10.0, 9.0],
          ['João', 5.0, 5.0, 5.0],
          ['José', 4.5, 2.5, 7.0]]

for nome, nota1, nota2, nota3 in alunos:
    media = (nota1 + nota2 + nota3) / 3
    print(f'{nome}:{media:.1f}')'''
    
#Questão 4 - Falar a média de cada aluno com a lista só para as notas (for):

#Método 1 (Kauê):

'''alunos = [['Ana', [7.5, 8.0, 8.5]],
          ['Maria', [8.0, 10.0, 9.0]],
          ['João', [5.0, 5.0, 5.0]],
          ['José', [4.5, 2.5, 7.0]]]

for nome, notas in alunos:
    media = (notas[0] + notas[1] + notas[2]) / 3
    print(f'{nome}:{media:.1f}')'''

#Método 2 (Professora):

'''alunos = [['Ana', [7.5, 8.0, 8.5]],
          ['Maria', [8.0, 10.0, 9.0]],
          ['João', [5.0, 5.0, 5.0]],
          ['José', [4.5, 2.5, 7.0]]]

for nome, notas in alunos:
    media = sum(notas)/ len(notas)
    print(f'{nome}:{media:.1f}')'''

#Método 3:

'''alunos = [['Ana', [7.5, 8.0, 8.5]],
          ['Maria', [8.0, 10.0, 9.0]],
          ['João', [5.0, 5.0, 5.0]],
          ['José', [4.5, 2.5, 7.0]]]

for nome, [n1, n2, n3] in alunos:
    media = (n1 + n2 + n3)/ 3
    print(f'{nome}:{media:.1f}')'''
