# Exercicio 7 - Calculo de Juros Simples

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

valor = float(input("Qual é o valor inicial do aporte? ").replace(',', '.'))
taxa = float(input("Qual é a taxa de juros anual (%)? ").replace(',', '.'))
anos = float(input("Quantos anos ficará aplicado? ").replace(',', '.'))

montante = valor + (valor * taxa * anos /100)

print("")
print("O Montante final será de: R$", montante)
print("")
print('-' * 80)