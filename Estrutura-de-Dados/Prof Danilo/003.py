
from tkinter.font import nametofont


print('-'*30)
print('CALCULADORA')
print('-'*30)

def soma(num):
    totsoma = num + 10
    return totsoma
    

def subtr(num):
    totsub = num - 7
    return totsub
    

def multi(num):
    totmult= num * 3
    return totmult
    

def div(num):
    totdiv= num / 2
    return totdiv
    

def pote(num):
    totpote= num ** 3
    return totpote

n1 = int(input('Informe um número: '))
fsoma = soma(n1)
print(f'{n1} + 10 : {fsoma}')

fsubtr=subtr(n1)
print(f'{n1} - 7 : {fsubtr}')

fmulti=multi(n1)
print(f'{n1} x 3 : {fmulti} ')

fdiv=div(n1)
print(f'{n1} / 2 : {fdiv}')

fpote=pote(n1)
print(f'{n1} ** 3 : {fpote}')

