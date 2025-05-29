# Exercico 3 - Conversão de Temperatura

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print('-' * 80)
print("")
temp1 = float(input("Quantos Graus Celsius pretende converter para Fahrenheit? ").replace(',','.'))
celsius = temp1

formula = (celsius *9/5) + 32.

print("")
print(f"{celsius}°C convertido para Fahrenheit é {formula}°F")
print("")
print('-' * 80)