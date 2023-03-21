dados = {}
dados['Nome'] = str(input('Digite o nome do aluno: '))
dados['Média'] = float(input(f'Digite a média de {dados["Nome"]}: '))
if dados['Média'] >= 6:
    dados['Situação'] = 'aprovado'
elif dados['Média'] < 6:
    dados['Situação'] = 'reprovado'
for i, v in dados.items():
    print(i, 'é igual a',v)