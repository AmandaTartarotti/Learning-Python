palavra = input("Digite algo:")
print('O tipo primitivo desse valor é', type(palavra))
print('Só tem espaços?', palavra.isspace())
print('É um número?', palavra.isnumeric())
print('É alfabético?', palavra.isalpha())
print('É alfanumérico?', palavra.isalnum())
print('Está em maiuscúlo?', palavra.isupper())
print('Está em minúsculo?', palavra.islower())
print('Está capitalizada?', palavra.istitle()) #ex.Python, tem maiúsculo na inicial