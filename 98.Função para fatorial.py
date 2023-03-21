def fatorial(num = 1, show = False):
    """
    ->Calculo de fatorial
    : param n: o número a ser calculado
    : param show: mostrar ou não o calculo
    : return: o valor do fatorial de um num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c == 1:
                print(f'{c} = ', end= "")
            else:
                print(f'{c}', end=" x ")
        f*= c
    return f
  
print(fatorial(5, True))