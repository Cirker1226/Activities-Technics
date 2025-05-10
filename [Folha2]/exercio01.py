# Exercio 01 - Verificação de Numero Par ou Impar

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 50)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

numero = int(input("Qual é o Número desejado? "))

print("")

if numero % 2 == 0:
   print("O Número",numero,"é um numero Par!")
else:
   print("O Número",numero,"é um numero Impar!")

print("")
print('-' * 50)