from random import randint
alunos = []
medias = []
maiormedia = [0]*2
mediaclasse = mediasuper = mediainf = 0

for i in range(10):
    alunos.append(str(input("Informe um nome de aluno: ")))
    medias.append(randint(0, 10))
    mediaclasse += medias[i]

    if i == 0:
        maiormedia[0] = alunos[i]
        maiormedia[1] = medias[i]
    if medias[i] >= 7:
        mediasuper += 1

    else:
        mediainf += 1
    if maiormedia[1] < medias[i]:
        maiormedia[0] = alunos[i]
        maiormedia[1] = medias[i]

mediaclasse /= 10

for i in range(10):
    print(f'{alunos[i]}:{medias[i]}')

print("Média classe:", mediaclasse)
print(f'Quantidade de alunos com nota maior ou igual a 7: {mediasuper}')
print(f'Quantidade de alunos com média menor que 7: {mediainf}')
print(f'Aluno com maior média: {maiormedia[0]}, sendo {maiormedia[1]}')
