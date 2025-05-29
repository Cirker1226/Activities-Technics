# Exercicio 8 - Conversão de idades

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

anos = float(input("Quantos anos? ").replace(',','.'))

print("")

meses = anos * 12
dias = anos * 365

print(anos, "Anos equivale a", meses, "meses ou", dias, "dias.")
print("")
print('-' * 80)