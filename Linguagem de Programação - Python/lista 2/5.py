produtos = []
valores = []
mediavalor = 0
inf10 = 0
acima = 0
maiorvalor = [0, '']

for c in range(5):
    produtos.append(str(input('Digite o nome do produto: ')))
    valores.append(float(input('Digite o valor do produto: ')))

    if valores[c] < 10:
        inf10 += 1

    if valores[c] > maiorvalor[0]:
        maiorvalor[0] = valores[c]
        maiorvalor[1] = produtos[c]

    mediavalor = valores[c]
mediavalor /= 5

for i in range(5):
    if valores[i] > mediavalor:
        acima += 1

print('----- Compras realizadas -----')

for p in range(5):
    print('Produto: {} - R${:.2f}'.format(produtos[p], valores[p]))

print('Quantidade de produtos abaixo de  R$ 10,00: {}'.format(inf10))
print('Média dos valores: {}'.format(mediavalor))
print('Quantidade de produtos com valor acima da média: {}'.format(acima))
print('Produto com maior preço: {}, R${:.3f}'.format(maiorvalor[1], maiorvalor[0]))
