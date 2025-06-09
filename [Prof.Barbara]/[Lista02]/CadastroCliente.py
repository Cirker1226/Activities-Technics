import os
os.system('cls' if os.name == 'nt' else 'clear')

# Listas

clientes = []
gastos = []

# Pedindo as informaçoes dos clientes

i = 0

while True:
    print("-"*80)
    print("")
    print("Supermercados LMA - 24Hrs".center(80))
    print("")
    print("-"*80)
    print("")

    while True:
        nome = input(f"Qual é o nome do {i+1}º cliente? ").strip()
        if nome == "":
            print("Campo vazio. Por favor, digite um nome válido!")
        else:
            print("Cliente cadastrado com sucesso!")
            clientes.append(nome)
            break

    while True:
        try:
            valor = float(input(f"Qual é o valor total gasto pelo {i+1}º cliente? R$").replace(",","."))
            if valor == 0:
                print("Porfavor digite um valor maior do que 0!")
            else:
                gastos.append(valor)
                break
        except ValueError:
            print("Porfavor digite um valor válido!")

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Continuar ou sair

    i = i + 1  # Incrementa o contador de alunos

    print("-"*80)
    print("")

    continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().lower()
    if continuar != 's':
        break

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Exibindo os dados coletados

print("")
print("-" * 80)
print("")
print("Supermercados LMA - 24Hrs".center(80))
print("")
print("-" * 80)
print("")
print("Clientes cadastrados:".center(80))
print("")

for i in range(len(clientes)):
    print(f"{i+1}º: {clientes[i]} - R${gastos[i]}")

print("")
print("-"*80)
print("")

# Faturamento total

faturamento = sum(gastos)
print(f"O Faturamento total do dia é de R${faturamento:.2f}")

# Cliente que mais gastou

cliente_plus_valor = max(gastos)
indice_cliente_plus = gastos.index(cliente_plus_valor)
cliente_plus_nome = clientes[indice_cliente_plus]

print(f"O cliente que mais gastou foi {cliente_plus_nome} - R${cliente_plus_valor:.2f}")
print("")
print("-"*80)
