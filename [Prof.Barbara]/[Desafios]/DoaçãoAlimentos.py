import os, time
os.system('cls' if os.name == 'nt' else 'clear')

# Pedindo ao usuario a quantidade de kg de aimentos doados

while True:
    try:
        print("-" * 80)
        print("")
        kg = float(input("Quantos kg de alimentos foram doados? ").replace(",", "."))
        print("")
        print("-" * 80)
        break
    except ValueError:
        print("Por favor, insira um número válido.")

# Verificando se a doação é válida (1kg ou mais)

if kg < 1:
    print("\nDoação inválida! A doação deve ser de pelo menos 1kg.")
else:
    print(f"\nObrigado pela doação de {kg} kg(s) de alimentos!")
    print("\nAtualizando banco de dados...")

    time.sleep(3)

# Limpar terminal

os.system('cls' if os.name == 'nt' else 'clear')

# Listas

pacotes = [5, 2, 1]

# Calculando a quantidade de pacotes necessários

print("-"*80)
print("")
print("BANCA DE ALIMENTOS - BH".center(80))
print(f"Contabilizando a quantidade de pacotes necessarias!".center(80))
print("")

for pacote in pacotes:
    quantidade = kg // pacote
    kg = kg % pacote  # Atualizando a quantidade de kg restantes
    quantidade = int(quantidade)  # Convertendo para inteiro.
    if quantidade > 0:
        print(f"A doação total será divida em {quantidade} pacote(s) de {pacote} kg(s).".center(80))

kg_restante = kg
kg_restante = round(kg_restante, 2)

print("")
print(f"Quantidade de alimentos restantes: {kg_restante} kg(s)".center(80))
print("Obrigado por contribuir com a nossa causa!".center(80))
print("")
print("-"*80)
