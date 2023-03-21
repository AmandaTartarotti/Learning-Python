palvras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRÁTIS','ESTUDAR','PRÁTICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for item in palvras:
    print(f'\nNa palvra {item} temos',end=" ") #\n quebra a linha
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=" ")