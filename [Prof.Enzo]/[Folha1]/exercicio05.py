# Exercicio 5 - Cáluco de IMC

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

peso = float(input("Quantos Kg voce pesa? ").replace(',','.'))
altura = float(input("Quantos Metros voce tem? ").replace(',','.'))

imc = peso / (altura * altura)

# Arredondar os valores para 2 casas decimais
imcf = round(imc, 2)

print("")
print("O Seu Índice de Massa corporal é:", imcf, "kg/m²")
print("")
print('-' * 80)
