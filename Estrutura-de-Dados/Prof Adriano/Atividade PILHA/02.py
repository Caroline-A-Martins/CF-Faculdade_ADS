expressao = input('Digite a sequência de parênteses a validar: ')
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] in '({[':
        pilha.append(expressao[x])
    elif expressao[x] == ')':
        if len(pilha) > 0 and pilha[-1] == '(':
            pilha.pop()
        else:
            pilha.append(')')
            break
    elif expressao[x] == ']':
        if len(pilha) > 0 and pilha[-1] == '[':
            pilha.pop()
        else:
            pilha.append(']')
            break
    elif expressao[x] == '}':
        if len(pilha) > 0 and pilha[-1] == '{':
            pilha.pop()
        else:
            pilha.append('}')
            break
    x += 1

if len(pilha) == 0:
    print("OK")
else:
    print("Erro")
