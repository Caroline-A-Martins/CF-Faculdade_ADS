
p1= p2 = media = listas = 0
def cmedia(n1,n2,lis):
        media = n1*0.35+ n2*0.35 + lis*0.3
        return media

p1=float(input('Informe a nota da P1: '))
p2=float(input('Informe a nota da P2: '))
listas= float(input('Informe sua nota nas listas: '))

media=cmedia(p1,p2,listas)
if media >= 6:
    print('Parabens! Você está aprovado.')
    print('Sua média foi {:.2f}'.format(media))
else:
    print('Você está reprovado.')
    print('Terá que fazer SUB.')

    if p1 > p2:
        sub= float(input('Informe a nota da SUB: '))  
       
    media=cmedia(sub,listas)
    if media >= 6:
        print('Parabens! Você está aprovado.')
    else:
        print('Você está reprovado.')




