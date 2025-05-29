# Exercicio 4 - Numero positivo, negativo ou zero

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

numero = float(input("Digite um Número: ").replace(',','.'))
print("")

if numero > 0:
   print("O número digitado é um número positivo")
elif numero < 0:
   print("O número digitado é um número negativo")
else:
   print("O número digitado é nulo, ou seja, é igual a zero.")

print("")
print('-' * 80)
