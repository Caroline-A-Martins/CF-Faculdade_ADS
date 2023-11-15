primos = 0
somamult3 = 0
mediapares = 0
quantpares = 0
mult = 0
for c in range(10):
    num = int(input('Número: '))
    print(num)
    for i in range(1, num + 1):
        if num % i == 0:
            mult += 1
        if mult == 2:
            primos += 1
        if num % 3 == 0:
            somamult3 += num
        if num % 2 == 0 and num > 20:
            mediapares += num
            quantpares += 1

if mediapares > 0:
    mediapares /= quantpares
print('Quantidade de números primos: {}'.format(quantpares))
print('Soma dos numeros multiplos de 3: {}'.format(somamult3))
print('A média dos números pares maiores que 20: {}'.format(mediapares))
