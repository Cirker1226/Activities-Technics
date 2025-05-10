# Exercicio 5 - Classificação dos Triangulos.

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

lado1 = int(input("Qual é o valor do primeiro Lado? "))
lado2 = int(input("Qual é o valor do segundo Lado? "))
lado3 = int(input("Qual é o valor do terceiro Lado?" ))

print("")

if lado1 == lado2 == lado3:
  print("Esse triangulo é um triangulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("Esse triangulo é um triangulo isoceles.")
else:
  print("Esse triangulo é um triangulo Escaleno.")

print("")
print('-' * 80)

