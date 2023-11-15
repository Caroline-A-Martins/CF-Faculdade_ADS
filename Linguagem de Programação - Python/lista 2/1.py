listaidade = []
menor = maior = entre = media = 0
for c in range(6):
    listaidade.append(int(input('Informe sua idade: ')))
    if c == 1:
        entre = menor = maior = listaidade[c]
    else:
        if listaidade[c] > maior:
            maior = listaidade[c]
        if listaidade[c] < menor:
            menor = listaidade[c]
        if 20 <= listaidade[c] <= 30:
            entre = listaidade[c]

    media += listaidade[c]
media /= c

print('--' * 15)
print('Menor idade : {}'.format(menor))
print('Maior idade: {}'.format(maior))
print('Média das idades: {:.2f}'.format(media))
print('Pessoas com idade entre 20 e 30: {}'.format(media))



