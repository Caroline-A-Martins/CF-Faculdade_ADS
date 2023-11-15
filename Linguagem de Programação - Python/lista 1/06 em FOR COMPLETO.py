maioridade = 0
menoridade = 0
media = 0
entre = 0
e = 0

for c in range(0, 3):
    idade = int(input('Idade: '))
    if c == 0:
        menoridade = idade
    if idade > maioridade:
        maioridade = idade
    if idade < menoridade:
        menoridade = idade
    if 20 <= idade <= 40:
        entre = idade
        e += 1
    media += idade
media /= (c + 1)

print('{:.2f} é a maior idade.'.format(maioridade))
print('{:.2f} é a menor idade.'.format(menoridade))
print('{} é a quantidade de pessoas que têm entre 20 e 40 anos.'.format(e))
print('A média das idade é {:.2f}'.format(media))

