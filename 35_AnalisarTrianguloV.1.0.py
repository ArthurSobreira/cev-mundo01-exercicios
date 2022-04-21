print('=-' * 20)
print('Analizador de triângulos')
print('=-' * 20)
r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Com três retas de medidas: {r1}, {r2} e {r3}, é possível formar um triângulo.')
else:
    print(f'Com três retas de medidas: {r1}, {r2} e {r3}, não é possível formar um triângulo. ')
