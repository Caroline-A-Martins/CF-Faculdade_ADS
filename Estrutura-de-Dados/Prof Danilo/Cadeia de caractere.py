
print('ESCREVA UMA FRASE')
frase = str(input('')).upper().strip()

vog=['A','E','I','O','U']
cons= ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vogais= 0
consoantes=0

def vogecon(frase):
    for c in range(len(frase)): 
        if frase[c] in vog:
            vogais +=1
            print(f'N° DE VOGAIS: {vogais} ')
        if frase[c] in cons:
            consoantes+=1
        return frase

nums='147'
acresnum = nums+frase

let='SMD'
acreslet = frase+let


    



        

