nome = str(input('Digite seu Nome:')).strip()
print(f'Nome com todas as letras Maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras Minúsculas: {nome.lower()}')
esp = nome.count(' ')
num = len(nome) - esp
print(f'Seu nome possui {num} letras')
div = nome.split()
print(f'Seu primeiro nome possui {len(div[0])} letras')
