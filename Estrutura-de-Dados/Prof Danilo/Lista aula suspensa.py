
'''Lista aula suspensa
Baseado no conceito de orientação a objetos e os exemplos, 
crie uma rotina que realize a venda de um produto.
Para isto, crie uma classe cliente, 
uma classe produto e
uma classe venda, 
está última incorporando atributos e ou métodos das outras classes.
'''



class Cliente:# qnt de dinheiro, nome
    id = None 
    nome =  None
    def imprime(self):
        print (f'O nome é {self.nome}')
        print(f'O id {self.id}')

class Produto: # nome do produt, valor
    valor = None
    def custo(self):
        print(f'Valor do produto: {self.valor}')

class Venda: # se a venda é realizada
    def comprar(self):
        resp = str(input('Realizar compra?'))
        if resp != 'SIM' and resp !='sim':
            print('Compra não realizada')
        else:
            print('Compra realizada')



cliente=Cliente()
cliente.id = str(input('ID: '))
cliente.nome = str(input('NOME: '))
cliente.imprime()

produto=Produto()
produto.valor = str(input('R$: '))
produto.custo()

venda=Venda()
venda.comprar()
