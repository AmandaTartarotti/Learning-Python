def notas(*valor,sit=False): #valor vira uma tupla
    dic = {}
    dic["total"] = len(valor)
    dic["maior"] = max(valor)
    dic["menor"] = min(valor)
    soma = 0
    for i in valor:
        soma += i
    média = soma / len(valor)
    dic["média"] = média
    if sit:
        if média >= 7:
           sit = "BOM"
        elif média >= 5:
            sit = 'RAZOAVEL'
        else:
            sit = 'RUIM'
        dic["situação"] = sit
    return dic

#Programa Principal
resp = notas(5.5,2.5,1.5, sit = False)
print(resp)