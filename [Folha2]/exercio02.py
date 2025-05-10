# Exercio 02 - Maior entre dois numeros

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

numero1 = float(input("Digite o primeiro valor: ").replace(',','.'))
numero2 = float(input("Digite o segundo valor: ").replace(',','.'))

print("")

if numero1 > numero2:
   print("O número",numero1,"é maior que o número",numero2)
elif numero1 < numero2:
   print("O número", numero2,"é maior que o número",numero1)
else:
   print("Os números digitados são Iguais!")

print("")
print('-' * 80)
print("")