from datetime import date
import datetime
count = 0
menor = 0
maior = 0
for a in range(1,8):
    count += 1
    b = int(input('Em que ano nasceu a {}º pessoa?'.format(count)))
    c = datetime.date.today().year
    if c - b < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maior de idade.'.format(maior))
print('Ao todo tivemos {} pessoas menor de idade.'.format(menor))