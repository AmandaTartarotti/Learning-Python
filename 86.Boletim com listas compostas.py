lista = []
valores = []
while True:
        lista.append(str(input('Digite o nome do aluno: ')))
        lista.append(float(input('Digite a primeira nota do aluno: ')))
        lista.append(float(input('Digite a segunda nota do aluno: ')))
        valores.append(lista[:])
        lista.clear()
        a = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if a == 'n':
            break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') #4 e 10 caracteres alinhados a esquerda, 8 alinhado a esquerda
print(f'-'*50)
for count, value in enumerate(valores, start=1):
    media = (value[1]+value[2])/2
    print(f'{count:<4}{value[0]:<10}{media:>8}')
while True:
    print(f'-'*50)
    b = int(input('Mostrar a nota de qual aluno? (999 interrompe) '))
    if b == 999:
        break
    for count, value in enumerate(valores,start = 1):
        if b == count:
            print('As notas de {} são: {} e {}'.format(value[0],value[1],value[2]))
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')