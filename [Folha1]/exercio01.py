# Exercicio 1 - Soma de dois numeros

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print('-' * 80)
print("")

numero1 = float(input("Digite o primeiro Numero: ").replace(',','.'))
numero2 = float(input("Digite o segundo Numero: ").replace(',','.'))
resultado = numero1 + numero2

# Arredondar os valores para 2 casas decimais
resultadof = round(resultado, 2)

print("")
print("A soma final dos dois números é:", resultadof)
print("")
print('-' * 80)

