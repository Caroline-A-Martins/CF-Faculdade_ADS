from random import randint

li1 = []
li2 = []
rept = []
uni = []
for c in range(5):
    li1.append(randint(1, 15))
    li2.append(randint(1, 15))

for c in range(5):
    if li1[c] in li2:
        rept.append(li1[c])
    if li2[c] in li1:
        rept.append(li2[c])

    if li1[c] not in li2:
        uni.append(li1[c])

print(li1)
print(li2)
print(f'Números repetidos: {rept}')
print('Números unicos: {}'.format(uni))




