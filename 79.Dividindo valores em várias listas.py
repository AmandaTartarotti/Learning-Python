lista = []
lista_pares = []
lista_ímpares =[]
while True:
    valores = int(input('Digite um número: '))
    if valores % 2 == 0:
        lista_pares.append(valores)
    else:
        lista_ímpares.append(valores)
    lista.append(valores)
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_ímpares}')