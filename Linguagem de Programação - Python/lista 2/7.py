from random import randint

li1 = []
li2 = []
soma = []
for a in range(5):
    li1.append(randint(1, 11))
    li2.append(randint(1, 11))

for b in range(5):
    soma.append(li1[b] + li2[b])

print('Elementos da lista 1: {}'.format(li1))
print('Elementos da lista 2: {}'.format(li2))
print('A soma dos elementos da lista 1 e da lista 2: {}'.format(soma))





