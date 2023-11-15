import re


def totdesloc (n1,n2): #
    tot = n1 *(n2 * 0.51) 
    return tot
    
def pessoajuri(n1): # adicionar 30% no total
    tot = n1 +(n1 * (30/100))
    return tot

def pessoafisica(n1): # descontar 6% do total;
    tot = n1 - (n1 * (6/100))
    return tot

def pessoaclt(n1):  # adicionar 8% de periculosidade e descontar 5% de INSS do total.
    peri = n1 + (n1 * (8/100))
    tot = peri - (n1 * (5/100))
    return tot

def descontos(n1,n2):
    des = n1-n2
    return des


nome = str(input('Digite o nome do funcionario: '))
hrs = int(input('Horas de trabalho: '))
desloc = float(input('N° de deslocamento: '))
km = float(input('Quilometros rodados: '))
hrsalario = float(input('Quanto recebe por hora: '))
print('Tipo de Funcionário: \n'
      '[ 1 ] Pessoa Jurírdica \n'
      '[ 2 ] Pessoa Física \n'
      '[ 3 ] Contratado por CLT \n')
opt = int(input('Qual é o tipo de contração do seu funcionário: '))

# contas
tot_salario = hrs * hrsalario
tot_desloc = desloc * km

if opt == 1:
    pessjuridica = pessoajuri(tot_salario)
    desconto = descontos (pessjuridica, tot_salario)
    print('Seu salario teve um aumento de 30%')
    print(f'SALARIO ANTIGO: {tot_salario:.2f}')
    print(f'NOVO SALARIO: {pessjuridica:.2f}')
    print(f'DESCONTOS: {desconto:.2f}')

if opt == 2:
    pessfisica = pessoafisica(tot_salario)
    desconto = descontos (pessfisica, tot_salario)
    print('Seu salario teve um desconto de 5%')
    print(f'SALARIO ANTIGO: {tot_salario:.2f}')
    print(f'NOVO SALARIO: {pessfisica:.2f}')
    print(f'DESCONTOS: {desconto:.2f}')

    

if opt == 3:
    pessclt = pessoaclt(tot_salario)
    desconto = descontos (pessclt, tot_salario)
    print('Seu salario teve um aumento de 8% e desconto de 6%')
    print(f'SALARIO ANTIGO: {tot_salario:.2f}')
    print(f'NOVO SALARIO: {pessclt:.2f}')
    print(f'DESCONTOS: {desconto:.2f}')













