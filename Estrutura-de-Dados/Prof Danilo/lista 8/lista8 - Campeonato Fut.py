from random import randint 

def Tabela():
    lista_completa=[]
    for i in range(10):
        n=[]
        n.append(f'Time {i + 1}')
        n.append(randint(1, 100))
        n.append(randint(1, 100))
        lista_completa.append(n)
    print('Tabela Sem ordenação')
    for item in lista_completa:
        print(item)
    print('')
    return lista_completa

    
def Ordenar(lista_completa):
    sorter = lambda x: (x[1], x[2], x[0])
    array = sorted(lista_completa, key=sorter)
    ordenedArray = array[::-1]
    print('Tabela com ordenação')
    for item in ordenedArray:
        print(item)
    return ordenedArray

lista_completa=Tabela()
arrayOrdenado=Ordenar(lista_completa)