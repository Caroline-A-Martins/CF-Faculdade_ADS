def potencia(a, b):
    if b == 0:
        return 1
    elif b < 0:
        raise ValueError("Não é permitido o expoente ser negativo")
    else:
        return a * potencia(a, b-1)


print(potencia(2, 3))
print(potencia(5, 0))
print(potencia(3, -2))
