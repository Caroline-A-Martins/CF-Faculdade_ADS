

for c in range(3):
    num = int(input('Digite um número para ver o seu Fatorial. '))
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    print('O fatorial de {} é {}'.format(num, fat))

