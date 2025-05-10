# Exercicio 2 - Média de Tres notas

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print('-' * 80)
print("")
nota1 = float(input("Qual é a primeira Nota? ").replace(',','.'))
nota2 = float(input("Qual é a segunda Nota? ").replace(',','.'))
nota3 = float(input("Qual é a terceira Nota? ").replace(',','.'))

notas = [nota1, nota2, nota3]
notaf = sum(notas)
media = notaf / len(notas)

# Arredondar os valores para 2 casas decimais
mediaf = round(media, 2)

print("")
print("A Media das Tres notas é:", mediaf)
print("")
print('-' * 80)
