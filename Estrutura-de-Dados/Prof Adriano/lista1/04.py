


def par_impar (x):
    if x % 2 == 0:
        return 'par'
    else:
       return 'ímpar'


y = int(input('Informe um valor'))
print(f'{y} é {par_impar(y)}')