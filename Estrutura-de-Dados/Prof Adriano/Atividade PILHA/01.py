# pilhas originais
pilha1 = ['Manga', 'Uva', 'Banana', 'Maçã', 'Pera', 'Laranja']
pilha2 = ['Abacate', 'Mamão', 'Melancia', 'Kiwi', 'Morango', 'Abacaxi']

# removendo a manga e a uva 
pilha1.remove('Manga')
pilha1.remove('Uva')

# obtendo as posições originais da manga e da uva
pos_manga = 0 if 'Manga' not in pilha1 else pilha1.index('Manga')
pos_uva = 0 if 'Uva' not in pilha1 else pilha1.index('Uva')

# inserindo a manga e a uva na pilha2 nas mesmas posições
pilha2.insert(pos_manga, 'Manga')
pilha2.insert(pos_uva, 'Uva')

# removendo o abacaxi e o morango da pilha2
pilha2.remove('Abacaxi')
pilha2.remove('Morango')

# obtendo as posições originais do abacaxi e do morango
pos_abacaxi = 0 if 'Abacaxi' not in pilha2 else pilha2.index('Abacaxi')
pos_morango = 0 if 'Morango' not in pilha2 else pilha2.index('Morango')

# inserindo o abacaxi e o morango na pilha1 nas mesmas posições
pilha1.insert(pos_abacaxi, 'Abacaxi')
pilha1.insert(pos_morango, 'Morango')

# exibindo as pilhas resultantes
print('Pilha 1 :', pilha1)
print('Pilha 2 :', pilha2)
