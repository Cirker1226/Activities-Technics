# Exercicio 06 - Aprovado ou Reprovado

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

nota = float(input("Qual é a nota apurada? ").replace(',','.'))
disciplina = str(input("Qual é a disciplina? "))

print("")

if nota >= 7:
   print(f"Você foi aprovado no exame de {disciplina}!")
else:
   print(f"Você foi reprovado no exame de {disciplina}!")

print("")
print('-' * 80)
