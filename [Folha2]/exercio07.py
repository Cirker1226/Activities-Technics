# Exercicio 07 - Verificação de Número Divisível por 3 e 5

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

numero1 = int(input("Qual é o Numero desejado? "))

print("")

if numero1 % 3 == 0 and numero1 % 5 == 0:
    print("O número digitado é divisível por 3 e 5 ao mesmo tempo.")
elif numero1 % 3 == 0 and numero1 % 5 != 0:
    print("O número digitado é divisível apenas por 3.")
elif numero1 % 3 != 0 and numero1 % 5 == 0:
    print("O número digitado é divisível apenas por 5.")
else:
    print("O número digitado não é divisível nem por 3 nem por 5.")

print("")
print('-' * 80)