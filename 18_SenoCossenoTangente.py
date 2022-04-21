import math

ang = float(input('digite o ângulo que você deseja: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'O ângulo {ang:.2f}º possui:')
print(f'Seno: {sen:.2f}\n'
      f'Cosseno: {cos:.2f}\n'
      f'Tangente: {tan:.2f}')
