from random import randint
li1 = []
li2 = []
li3 =[]
perfeito = 0
for i in range(5):
    li1.append(randint(1, 50))
    li2.append(randint(1, 50))
li3 = li1 + li2
for c in range(len(li3)):
    soma = 0
    for i in range (1, li3[c]):
        if li3[c] % i == 0:
            soma += i
    if li3[c] == soma:
        perfeito += 1
print(li3)
print("Quantidade de números perfeitos {}".format(perfeito))




