prod = float(input('Digite o preço do produto: R$'))
porcent = prod * 0.05
desc = prod - porcent
print(f'Depois de um desconto de 5%, o produto ficará com R$ {desc:.2f}')
