# Exercicio 09 -  Cálculo de Desconto com condição

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

valor = float(input("Qual é o valor do Produto? ").replace(',','.'))
desconto = float(input("Qual é o desconto dado? ").replace(',','.'))

print("")


descontoi = (valor * desconto) / 100
preçoi = valor - descontoi

if valor > 100:
   print("O Valor final do produto será de: R$", str(preçoi).replace('.', ','), "contando com um desconto de: R$", str(descontoi).replace('.', ','))
else:
   print("O Valor final do produto será de: R$",valor,"pois o desconto so se aplica em compras acima de R$100,00!")

print("")
print('-' * 80)
print("")