vel = float(input('Qual a velocidade do carro:'))
if vel > 80:
    mult = (vel - 80) * 7
    print(f'Você está acima da velocidade permitida de 80km/h, e sua multa é de R${mult:.2f}')
else:
    print('Você estava abaixo da velocidade permitida de 80km/h, continue assim!')
print('Dirija com cuidado!!')
