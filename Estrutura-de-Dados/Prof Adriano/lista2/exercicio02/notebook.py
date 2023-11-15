class Notebook:
    def __init__(self, marca, modelo, m_ram, p_video, processador, disco):
        self.marca = marca
        self.modelo = modelo
        self.m_ram = m_ram
        self.p_video = p_video
        self.processador = processador
        self.disco = disco
        self.status = 'desligado'

    def iniciar(self):
        self.status = 'ligado'
        print('Notebook iniciado.')

    def reiniciar(self):
        self.status = 'desligado'
        print('Notebook reiniciado.')

    def atualizar(self):
        print('Atualizando sistema operacional...')
        print('Atualização concluída.')

    def informacoes(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Memória RAM:', self.m_ram)
        print('Placa de vídeo:', self.p_video)
        print('Processador:', self.processador)
        print('Disco:', self.disco)
        print('Status:', self.status)


notebook1 = Notebook('Dell', 'Inspiron 15 3000', '8GB', 'Intel UHD Graphics 620', 'Intel Core i5-1035G1', '512GB SSD')
notebook1.informacoes()    
notebook1.iniciar()
notebook1.atualizar()
notebook1.reiniciar()
notebook1.informacoes()
