a = str(input('Digite uma expressão: '))
pilha = []
for item in a:
    if item == '(':
        pilha.append('(')
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop() #retira último item da lista
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')