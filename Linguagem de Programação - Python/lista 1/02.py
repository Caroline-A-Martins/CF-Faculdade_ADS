somaprimo = 0
mediamult3 = 0
quantmult3 = 0
media30 = 0
quant30 = 0

for c in range(10):
    num = int(input('Número: '))
    print(num)
    mult = 0
    for i in range(1, num + 1):
        if num % i == 0:
            mult += 1
        if mult == 2:
            somaprimo += num
        if num % 3 == 0 and num > 10:
            mediamult3 += num
            quantmult3 += 1

        if 10 <= num <= 30:
            media30 += num
            quant30 += 1

if media30 > 0:
    media30 /= quant30
if mediamult3 > 0:
    mediamult3 /= quantmult3

print('A soma dos números primos: {}'.format(somaprimo))
print('Média dos nº multiplos de 3 maiores que 10: {}'.format(mediamult3))
print('Média dos números entre 10 a 30: {:.2f}'.format(media30))
