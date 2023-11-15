from random import randint

matriz = []
medias = []
mediaMult5 = maiorNum2 = mediaColuna4 = quant = quant5 = 0

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(randint(1,50))
    matriz.append(linha)

for i in range(5):
    print(matriz[i])

for i in range(5):
    soma = 0
    for j in range(5):
        if(i == 0 and j == 1):
            maiorNum2 = matriz[i][j]
        
        if(matriz[i][j] % 5 == 0):
            mediaMult5 += matriz[i][j]
            quant5 += 1
        
        if(j == 1 and matriz[i][j] > maiorNum2):
            maiorNum2 = matriz[i][j]
        
        if(i == 3):
            mediaColuna4 += matriz[i][j]
        
        if(matriz[i][j] % 2 == 0 and matriz[i][j] >= 10 and matriz[i][j] <= 15):
            quant += 1
        
        soma += matriz[i][j]
    medias.append(soma/5)

mediaColuna4 /= 5
mediaMult5 /= quant5

print("Média números múltiplos de 5: %.2f" % (mediaMult5))
print("Maior número da coluna 2: %d" % (maiorNum2))
print("Média dos números da 4º linha: %.2f" % (mediaColuna4))
print("Quantidade de números pares, >= 10, <= 15: %d" % (quant))
print("Média de números de cada linha da matriz: ")
print(medias)        
        

        