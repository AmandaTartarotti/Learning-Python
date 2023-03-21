import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.date.today().year - ano_nascimento
dados['CTPS'] = int(input('Carteira de Trabalho: (0 não tem) '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Idade da aposentadoria'] = (dados['Contratação'] + 35) - ano_nascimento
print('-='*30)
for i, v in dados.items():
    print(f'{i} tem o valor {v}')