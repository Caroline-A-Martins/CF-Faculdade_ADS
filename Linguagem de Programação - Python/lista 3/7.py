from random import randint
cidade = []
mediasalpopu = mediafilhos = quantfilhos = mediasalario = cont = 0
for i in range(10):
    linha = []
    linha.append(randint(1000, 10000))
    linha.append(randint(15, 50))
    linha.append(randint(0, 10))
    cidade.append(linha)

for i in range(10):
    print(cidade[i])

for i in range(10):
    mediasalpopu += cidade[i][0]
    mediafilhos += cidade[i][2]
    if 15 <= cidade[i][1] <= 25:
        quantfilhos += cidade[i][2]
    if 20 <= cidade[i][1] <= 30:
        mediasalario += cidade[i][0]
        cont += 1

mediafilhos /= 10
mediasalpopu /= 10
mediasalario /= cont
print("Média salário população:", mediasalpopu)
print("Média número de filhos:", mediafilhos)
print("Quantidade de filhos de pessoas de 15 a 25 anos:", quantfilhos)
print("Média de salário das pessoas de 20 a 30 anos:", mediasalario)
