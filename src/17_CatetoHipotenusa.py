import math

catop = float(input('Digite o comprimento do Cateto Oposto:'))
catad = float(input('Digite o comprimento do Cateto Adjacente:'))
hip = (math.pow(catop, 2)) + (math.pow(catad, 2))
rhip = math.sqrt(hip)
print(f'O comprimento da Hipotenusa deste triângulo é de {rhip:.2f}')

catop = float(input('Digite o comprimento do Cateto Oposto:'))
catad = float(input('Digite o comprimento do Cateto Adjacente:'))
hip = math.hypot(catop, catad)
print(f'O comprimento da Hipotenusa deste triângulo é de {hip:.2f}')
