
from random import randint
mat = []
for i in range(3):
    lista = []
    lista.append(randint(1, 20))# cod do prod
    lista.append(str(input("Informe o nome do produto: ")))
    lista.append(randint(1.00, 100.00))# valor 
    lista.append(randint(1, 50))# estoque
    mat.append(lista)

for i in range(3):
    print(mat[i])
print()

print('-='*30)
print(f'{"Pesquisa"}')
print('-='*30)

#Crie uma função onde o usuário digite um código e verifique 
# se este código de produto está cadastrado, se houver exiba o código o nome,
# valor do produto e a quantidade em estoque;



cod = str(input('Informe o codigo do produto desejado: '))
if cod in mat[i]:
    print(f"""
Codigo : {mat[cod][0]}
Produto: {mat[cod][1]}
Valor: R$ {mat[cod][2]}
Estoque:{mat[cod][3]} 
    """)  

    v = int(input('Quantos gostaria de comprar: '))
    if v <= mat[0][3]:
        valor = []
        estoque = []
        valor.append(mat[0][2] * v)
        estoque.append(mat[0][3] - v)

    elif v > mat[0][3]:
        print('A quantidade não existem estoque.Tente novamente.')
        v = int(input('Quantos gostaria de comprar: '))

    r = str(input("Deseja continuar? [S/N] "))
        
    while r != "Nn":
        if r in 'nN':
            print('Obrigasa pela compra!')
            break
        
        else:
            cod = int(input('Informe o codigo do produto desejado: '))
            if cod in mat[i]:
                
                print(f"""
Codigo : {mat[0][0]}
Produto: {mat[0][1]}
Valor: R${mat[0][2]}
Estoque:{estoque} 
                """)  
            v = int(input('Quantos gostaria de comprar: '))
            if v <= mat[0][3]:
                valor = []
                estoque = []
                valor.append(mat[0][2] * v)
                estoque.append(mat[0][3] - v)

            r = str(input("Deseja continuar? [S/N] "))
    


print('Compra finalizada!')






