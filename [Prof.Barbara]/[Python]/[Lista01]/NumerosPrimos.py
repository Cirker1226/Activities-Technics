import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-"*80)
print("")
print("Os numeros primos entre 1 e 100 são:".center(80))
print("")

for n in range (1, 101): # Pega todos os numeros entre 1 e 100 OBS: 101 pq o python le o 0 como um, ou seja tem que adicionar mais um no final.
    primo = True # Afirma que todos os numeros sao primos.
    for d in range (2, n):
        if n % d == 0:
            primo = False # Variavel para verificar se o numero é primo ou não.
            break # Quebra o Loop de repetição.
    if primo:
            print(n, end = ' ') # Exibe todos os primos coletados.

print("")
print("\n", "-"*80)
