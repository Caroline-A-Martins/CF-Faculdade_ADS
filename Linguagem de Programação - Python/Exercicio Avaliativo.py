from random import randint
mat = []
medias = []
media5 = 0
Qmed5 = 0
maior2 = 0
medcol4 = 0
entre1015=0

for i in range(5):
    linha=[]
    for c in range(5):
        linha.append(randint(1,30))
    mat.append(linha)

for i in range(5):
    print(mat[i])

'''Operações'''
for i in range(5):
    soma = 0
    for c in range(5):
        if(i == 0 and c == 1):
            maior2 = mat[i][c]

        if mat[i][c] % 5 == 0:
            media5 += mat[i][c]
            Qmed5+=1

        if c == 1 and mat[i][c] > maior2:
            maior2 = mat[i][c]
            
        if i == 3:
            medcol4 += mat[i][c]

        if mat[i][c] % 2 == 0 and mat[i][c] >= 10 and mat[i][c] <= 15:
            entre1015 +=1

        soma += mat[i][c]
    medias.append(soma/5)

medcol4 /= 5
media5 /= Qmed5

print(f'A média dos números múltiplos de 5: {media5}')
print(f'O maior número da 2° coluna: {maior2}')
print(f'Média dos números da 4° linha da matriz: {medcol4}')
print(f'Quantidade de números pares, maiores ou iguais a 10 e menores ou iguais a 15: {entre1015}')
print(f'Média dos números de cada linha da matriz: {medias}')