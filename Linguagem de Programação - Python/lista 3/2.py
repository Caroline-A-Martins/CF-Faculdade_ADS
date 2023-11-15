from random import randint
mat = []
entre1030 = 0
somapares10 = 0
somacoluna4 = 0
medialinha3 = 0
cont = 0
for i in range(4):
    linha = []
    for c in range(6):
        linha.append(randint(1, 35))
        n = linha[c]
        cont += 1
        if 10 <= n <= 30:
            entre1030 += 1
        if n > 10 and n % 2 == 0:
            somapares10 += n
        if c == 3:
            somacoluna4 += n
        if c == 2:
            medialinha3 += n
    mat.append(linha)
medialinha3 /= cont
print('-=' * 32)
for i in range(4):
    for c in range(6):
        print(f'[{mat[i][c]:^5}]', end='')
    print()
print('-=' * 32)
print(f'A quantidade de números que estão no intervalo entre 10 e 30: {entre1030}')
print(f'A soma dos números maiores que 10 e pares: {somapares10}')
print(f'A soma dos números que estão na quarta coluna da matriz: {somacoluna4}')
print('A média dos números da matriz que estão na terceira linha: {:.2f}'.format(medialinha3))
