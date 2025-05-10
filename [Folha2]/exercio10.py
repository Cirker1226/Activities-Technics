# Exercicio 10 -  Classificação de Idade.

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

idade = int(input("Qual é a idade a ser classificada? "))

print("")

if idade < 12:
    print("Classificação: Criança.")
elif 12 >= idade < 18:
    print("Classificação: Adolescente.")
elif 18 <= idade < 30:
    print("Classificação: Adulto Jovem.")
elif 30 >= idade < 60:
    print("Classificação: Adulto.")
else:
    print("Classificação: Idoso.")

print("")
print('-' * 80)
print("")