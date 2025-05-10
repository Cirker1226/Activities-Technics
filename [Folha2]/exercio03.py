# Exercio 03 - Verificação de idade para digir

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

idade = int(input("Quantos anos você tem? "))
print("")

if idade >= 18:
  print("De acordo com o CTB,você já tem idade para tirar a carteira de habilitação.")
else:
  print("De acordo com o CTB,você ainda não tem idade suficiente para obter a carteira de habilitação.")
  print("A idade mínima exigida para tirar a carteira de motorista é de 18 anos completos.")

print("")
print('-' * 80)
print("")