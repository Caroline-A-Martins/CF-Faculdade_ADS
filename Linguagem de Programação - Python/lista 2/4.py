from random import randint

listaA = []
listaB = []
rept = []
for num in range(5):
    listaA.append(randint(1, 11))
    listaB.append(randint(1, 11))

for c in range(5):
    if listaA[c] in listaB:
        rept.append(listaA[c])

print('Primeira lista: {}'.format(listaA))
print('Segunda lista: {}'.format(listaB))
print(f'Os elementos que se repetem nas listas: {rept}')





