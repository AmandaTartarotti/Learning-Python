lista = list()
média = 0
dados = {}
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    média += dados['Idade']
    lista.append(dados.copy())
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ').strip().lower()[0])
    if resp == 'n':
        break
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {média//len(lista):.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for dados in lista:
    if dados['Sexo'] == 'F':
        print(dados['Nome'],end=" ")
print('\n- Lista das pessoas a cima da média:')
for dados in lista:
    if dados['Idade'] > (média//len(lista)):
        print(f'Nome = {dados["Nome"]}; sexo = {dados["Sexo"]}; idade = {dados["Idade"]} ')
print('<< ENCERRADO >>')