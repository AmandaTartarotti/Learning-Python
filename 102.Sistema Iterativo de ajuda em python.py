def linha(n='\033[m'):
    print(n,'-'*80)
def comando(resp):
    linha('\033[44m')
    print('Acessando o manual do comando'.center(80))
    linha('\033[45m')
    return help(resp)

while True:
    linha('\033[42m')
    print('SISTEMA ITERATIVO DE AJUDA EM PYTHON'.center(80))
    linha('\033[42m')
    resp = str(input('\033[mFunção ou biblioteca: ')).strip().lower()
    if resp == 'fim':
        linha('\033[41m')
        print('ATÉ LOGO!'.center(80))
        linha('\033[41m')
        break
    else:
        comando(resp)