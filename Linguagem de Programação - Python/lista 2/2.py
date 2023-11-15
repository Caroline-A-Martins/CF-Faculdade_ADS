listacor = ['rosa', 'azul', 'vermelho', 'amarelo', 'verde', 'roxo',
            'branco', 'preto', 'verde escuro', 'azul claro']

c = 'SIM'
print('----- Pesquisa de cores -----')

while c == 'sim' or c == 'SIM':

    cor = str(input('Digite uma cor: '))

    if cor in listacor:
        posi = (listacor.index(cor))
        print(f'A cor {cor} está na posição {posi + 1}')
    else:
        print(f'A cor {cor} não se encontra na lista')
        print('Tente novamente')

    c = str(input('Deseja continuar? [sim/não]'))



