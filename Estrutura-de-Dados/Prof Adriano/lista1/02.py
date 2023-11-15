


def soma (x,y):
    resp = x + y
    return resp 

def subtração (x,y):
    resp = x - y
    return resp 

def multiplicação (x,y):
    resp = x * y
    return resp 

def divisão (x,y):
    resp = x / y
    return resp 


v1 = int(input("Digite um número: "))
v2 = int(input("Digite outro número: "))
print('=-'*15)
print(f"A soma dos números {v1} e {v2} é: {soma(v1,v2)}")
print(f"A subtração dos números {v1} e {v2} é: {subtração(v1,v2)}")
print(f"A multiplicação dos números {v1} e {v2} é: {multiplicação(v1,v2)}")
print(f"A divisão dos números {v1} e {v2} é: {divisão(v1,v2)}")


