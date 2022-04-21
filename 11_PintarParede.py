print('|||Programa para calcular a quantidade de litros de tinta necessários para pintar uma  parede|||')
alt = float(input('Qual a Altura da parede em metros:'))
larg = float(input('Qual a Largura da parede em metros:'))
area = (alt * larg)
lit = area / 2
print(f'Para pintar uma parede de {area}m² serão necessários {lit:.1f} litros de tinta')
