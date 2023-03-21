k = 0 #para somar
contador = 0 #para ver quantos valores foram somados
for i in range(1,501,2):
    if i % 3 == 0:
        k += i
        contador += 1
print(k)
print(contador)