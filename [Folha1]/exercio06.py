# Exercicio 6 - Calculo de Desconto

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

preço = float(input("Qual é o valor do produto? ").replace(',', '.'))
desconto = float(input("Qual é o desconto aplicado ao produto? ").replace(',', '.'))

descontoi = (preço * desconto) / 100
preçoi = preço - descontoi

# Arredondar os valores para 2 casas decimais
descontof = round(descontoi, 2)
preçof = round(preçoi, 2)

print("")
print("O Valor final do produto será de: R$", str(preçof).replace('.', ','), "contando com um desconto de: R$", str(descontof).replace('.', ','))
print("")
print('-' * 80)
