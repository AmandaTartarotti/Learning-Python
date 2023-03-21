a = float(input('Largura da parede:'))
b = float(input('Altura da parede:'))
print('Sua parede tem a dimensão de {:.1f} x {:.1f} e a sua área é de {:.2f}m^2.'.format(a, b, a*b))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta'.format((a*b/2)))