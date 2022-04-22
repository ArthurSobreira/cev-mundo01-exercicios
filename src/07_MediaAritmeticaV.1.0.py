print('|||Programa que mostra a média de um aluno|||')
nome = input('Digite o Nome do aluno:')
nota1 = float(input('Nota 1º Semestre:'))
nota2 = float(input('Noma 2º Semestre:'))
med = (nota1 + nota2) / 2
print(f'A média do aluno {nome} foi de {med:.2f} pontos')
