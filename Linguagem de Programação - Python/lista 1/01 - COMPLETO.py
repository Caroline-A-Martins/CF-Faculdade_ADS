menor = 0
parmaior = 0
impar = 0
mediaM = 0
mediat = 0
for c in range(1, 11):
    num = int(input('Número: '))
    print(num)
    if c == 1:
        menor = num

    if num < menor:
        menor = num

    if num % 2 == 0:
        if num > 10:
            parmaior += num
    else:
        impar += 1

    if num > 20:
        mediat += 1
        mediaM += num

mediaM = mediaM / mediat
print('Menor número: {} '.format(menor))
print('Resultado da soma dos números pares maiores que 10: {} '.format(parmaior))
print('Quantidade de números impares: {}'.format(impar))
print('Média dos números maiores que 20: {}'.format(mediaM))
