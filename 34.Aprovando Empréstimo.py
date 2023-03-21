a = float(input('Valor da casa: R$'))
c = float(input('Salário do comprador: R$'))
b = int(input('Quantos anos de finaciamento? '))
parcela = a/(b*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(a, b, parcela))
status = 'APROVADO' if parcela < 0.3*c else 'NEGADO'
print('Empréstimo {}!'.format(status))