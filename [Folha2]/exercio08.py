# Exercicio 08 - Verificar se é vogal

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

letra = input("Qual é a letra desejada? ").strip().lower()

print("")

vogais = ('a','e','i','o','u')

if letra in vogais:
  print("A Letra digitada é uma vogal.")
else:
  print("A Letra digitada é uma consoante.")

print("")
print('-' * 80)



