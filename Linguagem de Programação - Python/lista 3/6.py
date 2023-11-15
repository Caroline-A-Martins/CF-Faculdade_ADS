from random import randint
mat = []
for i in range(6):
    linha = []
    for c in range(10):
        linha.append(randint(1,50))
    mat.append(linha)
linha7 = [0]*10

for i in range(6):
    for c in range(10):
        linha7[c] += mat[i][c]
        if i == 5:
            print(f'Soma elementos da coluna {c} é {linha7[c]}')
mat.append(linha7)

print('-='*35)
for i in range(6):
    for c in range(10):
        print(f'[{mat[i][c]:^5}]', end='')
    print()
print('-='*35)