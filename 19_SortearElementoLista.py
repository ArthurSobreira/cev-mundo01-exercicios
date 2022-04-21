from random import choice

alu1 = str(input('Primeiro aluno:'))
alu2 = str(input('Segundo aluno:'))
alu3 = str(input('Terceiro aluno:'))
alu4 = str(input('Quarto aluno:'))
alu5 = str(input('Quinto aluno:'))
lis = [alu1, alu2, alu3, alu4, alu5]
esc = choice(lis)
print(f'O aluno selecionado foi {esc}')
