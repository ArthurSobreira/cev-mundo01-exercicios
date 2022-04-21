frase = str(input('Digite uma frase:')).strip().upper()
qntA = frase.count('A')
priA = frase.find('A') + 1
ultA = frase.rfind('A') + 1
print(f'A letra  A  aparece na frase {qntA} vez(es)')
print(f'A primeira letra  A  aparece na {priA}ª posição')
print(f'A ultima letra  A  aparece na {ultA}ª posição')
