# Exercicio 9 - Troca de valores

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

valor1 = float(input("Qual é o primeiro valor? ").replace(',','.'))
valor2 = float(input("Qual é o segundo valor? ").replace(',','.'))

seila = valor1
valor1 = valor2
valor2 = seila

print("")
print("Invertendo os valores, o primeiro valor ficaria:", valor1, "e o segundo:", valor2)
print("")
print('-' * 80)