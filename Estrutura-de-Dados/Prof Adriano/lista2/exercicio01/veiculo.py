class Veiculo:
    def __init__(self, modelo, cor, combustivel, cambio, ano, preco, vel_max):
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.cambio = cambio
        self.ano = ano
        self.preco = preco
        self.vel_max = vel_max

# Criando duas instâncias da classe Veiculo
veiculo1 = Veiculo('Civic', 'Preto', 'Gasolina', 'Automático', 2020, 95000, 220)
veiculo2 = Veiculo('Gol', 'Branco', 'Etanol', 'Manual', 2018, 40000, 180)

# Imprimindo os valores 
print('Veículo 1:')
print('Modelo:', veiculo1.modelo)
print('Cor:', veiculo1.cor)
print('Combustível:', veiculo1.combustivel)
print('Câmbio:', veiculo1.cambio)
print('Ano:', veiculo1.ano)
print('Preço:', veiculo1.preco)
print('Velocidade Máxima:', veiculo1.vel_max)

print('\nVeículo 2:')
print('Modelo:', veiculo2.modelo)
print('Cor:', veiculo2.cor)
print('Combustível:', veiculo2.combustivel)
print('Câmbio:', veiculo2.cambio)
print('Ano:', veiculo2.ano)
print('Preço:', veiculo2.preco)
print('Velocidade Máxima:', veiculo2.vel_max)
