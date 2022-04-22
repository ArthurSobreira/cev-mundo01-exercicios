sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    porc = sal * 0.15
    aum = sal + porc
    print(f'Após um aumento de 15%, seu salário será de R${aum:.2f}')
else:
    porc = sal * 0.10
    aum = sal + porc
    print(f'Após um aumento de 10%, seu salário será de R${aum:.2f}')
