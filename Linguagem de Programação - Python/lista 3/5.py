from random import randint
mat = []
somalinhas = somaprimos = 0

for i in range(4):
    linha = []
    for c in range(3):
        linha.append(randint(1, 50))
    mat.append(linha)

for i in range(4):
    for c in range(3):
        print(f'[{mat[i][c]:^5}]', end='')
    print()

for i in range(4):
    for c in range(3):
        mult = 0

        for k in range(1, mat[i][c] + 1):
            if mat[i][c] % k == 0:
                mult += 1

        if mult == 2:
            somaprimos += mat[i][c]
        if i == 1 or i == 3:
            somalinhas += mat[i][c]

print(f'Soma dos elementos da 2ª e 4ª linha: {somalinhas}')
print(f'Soma dos números primos: {somaprimos}')

