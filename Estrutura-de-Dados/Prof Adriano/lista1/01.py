


def verificar_positivo(num):
    if num > 0:
        return "P"
    else:
        return "N"


valor = int(input("Digite um número: "))
resultado = verificar_positivo(valor)
print(f"O resultado para o valor {valor} é: {resultado}")


