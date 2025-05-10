# Exercicio 4 - Calculo da Área de um Retangulo

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

altura = int(input("Qual é altura do Retangulo? "))
largura = int(input("Qual é a largura do Retanguo? "))

area = altura * largura

print("")
print("A Área total do Retangulo é:", area, "m²")
print("")
print('-' * 80)