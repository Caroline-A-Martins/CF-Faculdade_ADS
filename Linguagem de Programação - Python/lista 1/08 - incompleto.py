menor18 = 0
mediaIdade = 0
mediaAltura = 0
peso80 = 0
for t in range(1, 3):
    print('Informaçoes sobre o time {}'.format(t))

    for c in range(1, 4):
        print('Jogador {}'.format(c))
        idade = int(input('Idade: '))
        print(idade)
        altura = float(input('Altura: '))
        print(altura)
        peso = int(input('Peso: '))
        print(peso)

        if idade < 18:
            menor18 += 1

        mediaIdade += idade
        mediaAltura += altura
    mediaAltura /= 11

    print('Média das idades do time {}: {}'.format(t, mediaIdade))
print('Quantidade de jogadores menores que 10 anos: {}'.format(menor18))
print('Média das alturas dos jogadores: {}'.format(mediaAltura))
