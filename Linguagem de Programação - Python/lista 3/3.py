from random import randint
mat = []
total = []
maiorvenda1 = menorvenda3 = 0
for i in range(5):
    lista = []
    lista.append(str(input("Informe o nome do vendedor: ")))
    for c in range(3):
        lista.append(randint(1, 200))
    mat.append(lista)
for i in range(5):
    print(mat[i])
for i in range(5):
    soma = 0
    for c in range(1, 4):
        if i == 0 and c == 1:
            maiorvenda1 = mat[i][c]
        elif c == 1:
            if mat[i][c] > maiorvenda1:
                maiorvenda1 = mat[i][c]
        if i == 0 and c == 3:
            menorvenda3 = mat[i][c]
        elif c == 3:
            if mat[i][c] < menorvenda3:
                menorvenda3 = mat[i][c]
        soma += mat[i][c]
    total.append(soma)
for i in range(5):
    print(f"O vendedor {mat[i][0]} teve {total[i]} vendas no total")
print(f'Maior venda do mês 1: {maiorvenda1}')
print(f'Menor venda do mês 3: {menorvenda3}')

