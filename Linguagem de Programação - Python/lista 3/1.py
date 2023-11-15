from random import randint

matriz = list()
mult3 = scol = media = menor = maior = cont =0
for l in range(3):
    linha = []
    for c in range(5):
        linha.append(randint(1, 15))
    matriz.append(linha)
    media = matriz[l][c]
    cont +=1

print('-=' * 30)
for l in range(3):
    for c in range(5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

# menor numero
for l in range(3):
    for c in range(5):
        if matriz[l][c] == 0:
            menor = maior = matriz
        else:
            if matriz[l][c] > maior:
                maior += 1
            if matriz[l][c] < menor:
                menor += 1
print(f'Menor: {menor}')

# soma da 3° coluna
for l in range(3):
    scol += matriz[l][2]
print(f'A soma dos valores a 3° coluna é {scol}')

# soma dos mult de 3
for l in range(3):
    for c in range(5):
        if matriz[l][c] % 3 == 0:
            mult3 += 1
print(f'Soma dos mult de 3: {mult3}')

media /= cont
print(f'Média da matraz: {media}')
