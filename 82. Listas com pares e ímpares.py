valores = []
pares = []
ímpares = []
for i in range(1,8):
    valores.append((int(input(f'Digite o {i}º valor: '))))
for p in valores:
    if p % 2 == 0:
        pares.append(p)
    elif p % 2 == 1:
        ímpares.append(p)
pares.sort()
ímpares.sort()
print('='*30)
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores ímpares digitados foram {ímpares}')
