# Exercicio 10 - Calculadora de Média Ponderada

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

media1 = float(input("Qual é o valor da primeira nota?").replace(',','.'))
peso = float(input("Qual é o peso desejado para a primeira nota?").replace(',','.'))

print("")

media2 = float(input("Qual é o valor da segunda nota?").replace(',','.'))
peso2 = float(input("Qual é o segundo peso dejado para a segunda nota?").replace(',','.'))

print("")

media3 = float(input("Qual é o valor da terceira nota?").replace(',','.'))
peso3 = float(input("Qual é o terceiro peso desejado para a terceira nota?").replace(',','.'))

ponderada = (media1 * peso + media2 * peso2 + media3 * peso3) / (peso + peso2 + peso3)

# Arredondar os valores para 2 casas decimais
ponderadaf = round(ponderada, 2)

print("")
print("A Média ponderada de suas notas seria:", ponderadaf)
print("")
print('-' * 80)