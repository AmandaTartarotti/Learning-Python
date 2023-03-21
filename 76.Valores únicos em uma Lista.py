lista = []
while True:
    b = (int(input('Digite um valor: ')))
    if b in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista += [b]
        print('Valor adionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()
    if continuar == "n":
        break
print('='*30)
print(f'Você digitou os valores {lista}')