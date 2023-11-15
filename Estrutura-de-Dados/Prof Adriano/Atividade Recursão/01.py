def fatorial(x):
    if x <= 1:
        return 1
    else:
        return x * fatorial(x - 1)


valor = int(input('Digite um valor: '))
print(f'O fatorial {valor}: {fatorial(valor)}')
