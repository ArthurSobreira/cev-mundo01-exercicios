viaj = float(input('Qual a distância da viagem:'))
if viaj <= 200:
    pre = viaj * 0.5
    print(f'O preço por uma viagem de {viaj:.0f}Km é de R${pre:.2f}')
else:
    pre2 = viaj * 0.45
    print(f'O preço por uma viagem de {viaj:.0f}Km é de R${pre2:.2f}')
