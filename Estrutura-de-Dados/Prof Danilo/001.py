
p1= p2 = media = listas = 0


p1=float(input('Informe a nota da P1: '))
p2=float(input('Informe a nota da P2: '))
listas= float(input('Qual sua nota nas listas?'))

media = ((p1*0.35)+ (p2*0.35) + listas )
if media >= 6:
    print('Parabens! Você está aprovado.')
    print('Sua média foi {:.2f}'.format(media))
else:
    print('Você está reprovado.')
    print('Terá que fazer SUB.')

    if p1 > p2:
        p2= float(input('Informe a nota da SUB'))
    else:
        p1= float(input('Informe a nota da SUB'))
    media = ((p1*0.35)+ (p2*0.35) + listas )
    if media >= 6:
        print('Parabens! Você está aprovado.')
    else:
        print('Você está reprovado DEFINITIVAMENTE.')



