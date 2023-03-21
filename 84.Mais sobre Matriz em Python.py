matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma_col = soma_lin = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha],[coluna]}: '))
        if coluna == 2:
            soma_col += matriz[linha][coluna]
        if linha == 1:
            soma_lin += matriz[linha][coluna]
print('='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('='*30)
for item in matriz:
    for valor in item:
        if valor % 2 == 0:
            soma += valor
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma_col}.')
print(f'O maior valor da segunda linha é {soma_lin}.') 