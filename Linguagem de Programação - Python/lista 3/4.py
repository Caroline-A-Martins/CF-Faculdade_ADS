from random import randint
soma = 0
alunos = []
medias = []
status = []
for i in range(5):
    linha = list()
    linha.append(str(input("Informe o nome do aluno(a): ")))
    for c in range(2):
        linha.append(randint(0, 10))
    alunos.append(linha)

for i in range(5):
    print(alunos[i])

for i in range(5):
    soma = 0
    for c in range(1, 3):
        soma += alunos[i][c]
    medias.append(soma / 2)
print(f'Médias dos alunos(a): {medias}')

for i in range(5):
    if medias[i] >= 6:
        status.append("Aprovado")
    else:
        status.append("Reprovado")

print(status)
pesquisa = str(input("Insira o nome do aluno(a) que deseja pesquisar: "))

while pesquisa != "Nn":
    pesq = []
    for i in range(5):
        if alunos[i][0] == pesquisa:
            pesq.append(i)
            pesq.append(0)
            print(f'Aluno(a): {alunos[pesq[0]][pesq[1]]}; Posição: {pesq[0] + 1} e {pesq[1] + 1}')
            print(f'Nota 1: {alunos[pesq[0]][pesq[1] + 1]}; Nota 2: {alunos[pesq[0]][pesq[1] + 2]}')
            print(f'Média: {medias[pesq[0]]}')
            print(f'Status: {status[pesq[0]]}')
    r = str(input("Deseja continuar? [S/N] "))
    if r in 'nN':
        break
    pesquisa = str(input("Insira o nome do aluno(a) que deseja pesquisar: "))
