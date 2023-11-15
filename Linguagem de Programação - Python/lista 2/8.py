nomes = []
vendas = []
comissao = []
total = 0
media = 0
acima = 0
for c in range(5):
    nomes.append(str(input('Nome: ')))
    vendas.append(float(input('Informe o valor de vendas: ')))
for i in range(5):
    comissao.append(vendas[i] * 0.1)
    total += vendas[i]
for k in range(5):
    if vendas[k] > media:
        acima += 1
maior = max(comissao)
idx = comissao.index(maior)
nomeMaior = nomes[idx]
media = total / 5
for p in range(5):
    print('Vendedor(a) {}: R${:.2f}'.format(nomes[p], comissao[p]))
print('Total bruto: {:.2f}'.format(total))
print('Média do total de vendas: {:.2f}'.format(media))
print('Quantidade de vendedores com vendas acima da média: {}'.format(acima))
print('O vendedor {} teve a maior comissão, R${:.2f}'.format(nomeMaior, maior))




