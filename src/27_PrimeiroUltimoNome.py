nome = str(input('Digite seu nome completo:')).strip()
priN = nome.split()
print(f'Seu nome completo é: {nome}')
print(f'Seu primeiro nome é: {priN[0]}')
print(f'Seu último nome é: {priN[len(priN) - 1]}')
