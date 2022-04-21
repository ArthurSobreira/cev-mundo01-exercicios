import random
import time

n1 = random.randint(0, 5)
print('\033[97;1m=-=\033[m' * 27)
print('\033[36mO computador acaba de pensar em um número de 0 a 5, consegue adivinhar qual é:\033[m')
print('\033[97;1m=-=\033[m' * 27)
n2 = int(input('\033[97mDigite o número que pensa ser:\033[m'))
print('\033[33mProcessando...\033[m')
time.sleep(2)
if n2 == n1:
    print('\033[1;32mACERTOU!!\033[m, Meus Parabéns, seus chutes são muito bons!!')
else:
    print(f'\033[1;31mERROU!!\033[m, Essa foi perto, mas o número era {n1}!!')
print('\033[97;1m=-=\033[m' * 27)
