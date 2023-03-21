def leiaint(msg):
    valor = input(msg)
    while not valor.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.')
        valor = input('\033[mDigite um número inteiro: ')
    return valor

#Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')