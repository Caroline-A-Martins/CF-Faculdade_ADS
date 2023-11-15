otimo = 0
bom = 0
regular = 0
somaida = 0
media = 0
quant = 0

idade = int(input('Idade: '))
print(idade)
while idade > 0:
    print('''  [1] Ótimo
  [2] Bom
  [3] Regular''')
    opcao = int(input('Qual a sua opinião sobre o filme? '))
    print(opcao)

    if opcao == 1:
        otimo += 1

    if opcao == 2:
        bom += 1

    if opcao == 3:
        regular += 1

    if opcao > 3:
        print('Opção inválida. Tente novamente')

    media += idade
    quant += media

    idade = int(input('Idade: '))
    print(idade)

    if media > 0:
        media /= quant

print('{} pessoas acharam o filme Ótimo'.format(otimo))
print('{} pessoas acharam o filme Bom'.format(bom))
print('{} pessoas acharam o filme Regular'.format(regular))
print('A média das idades das pessoas que assistiram o filme é {:.2f}'.format(media))
