def desconto20 (num):
    tot = num - (num * (20/100)) #Menos 20 por cento
    return tot

def desconto15 (num):
    tot = num - (num * (15/100))
    return tot

def desconto5(num):
    tot = (num - (num * (5/100)))/2
    return tot

def acrescimo5 (num,parc):
    tot = (num + (num*5/100))/parc
    return tot

totroupa = totsapato = 0

prod = str(input('Você gostaria de comprar roupas ou sapatos? '))
devedor = str(input('Você é um devedor: [s/n]  ')) # verificando se é um devedor
if devedor == "sS":
    print('Você só pode comprar a vista')
    if prod =='roupas' or prod == 'roupa':
        totroupa = float(input('Qual foi o valor total da sua compra:  '))
        print('Compra realizada!')
        
    if prod == 'sapato' or prod == 'sapatos':
        totsapato = float(input('Qual foi o valor total da sua compra:  '))
        pagamento = str(input('Qual a forma de pagamento, cheque ou dinheiro: '))

        if pagamento != 'cheque' or pagamento != 'CHEQUE': # conferindo se é em cheque ou dinheirp
            pagcheque=desconto15(totsapato)
            print(f'Sua compra de {totsapato} com desconto de 15% deu {pagcheque}')


        else: 
            pagdinheiro = desconto20(totsapato)
            print(f'Sua compra de {totsapato} com desconto de 20% deu {pagdinheiro}')


if devedor != 'sS': # caso não seja um devedor
    if prod =='roupas' or prod == 'roupa':
        totroupa = float(input('Qual foi o valor total da sua compra:  '))
        print('Compra realizada!')
        
        
    if prod == 'sapato' or prod == 'sapatos':
        totsapato = float(input('Qual foi o valor total da sua compra:  '))
        parcela = int(input('Gostaria de dividir em quantas parcelas: ')) # num de parcelas
        #conferindo descontos
        if parcela == 2:
            parcela2 = desconto5(totsapato) / 2
            print(f'Sua compra de {totsapato} parcelado em 2x com desconto de 5% deu {parcela2}')

        if parcela == 3:
            print(f'Sua compra de {totsapato} parcelado em 3x sem desconto deu {totsapato/3}')

        if parcela >= 4: #n esta cauculando o acrescimo
            acres5 = acrescimo5(totsapato,parcela)
            print(f'Sua compra de {totsapato} parcelado em {parcela} com acréscimo de 5% deu {acres5}')




            

    







