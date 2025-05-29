import os
os.system('cls' if os.name == 'nt' else 'clear')

# Pedindo ao usuario a quantidade de itens

while True:
    try:
        print("-"*80)
        print("")
        quantidade = int(input("Qual é a quantidade de itens a adicionar na Lista de Compra? "))
        print("")
        print("-"*80)
        break
    except ValueError:
        print("Porfavor, digite um número inteiro válido!")

# Lista dos itens adicionados

itens = []
quantidade_itens = []

# Pedindo as informaçoes dos itens

for i in range (quantidade):
    while True:
            item = input(f"\n Qual é o {i +1}º Item a ser adicionado em sua Lista de Compra? ")

            if item.strip() == "":
                print("Campo vazio. Digite um item válido.")
            else:
                print("Item cadastrado com sucesso. \n")
                itens.append(item)
            break

    while True:
        try:
            quantidade_item = int(input(f"Qual é a quantidade do {i +1}º a ser comprada? "))
            if quantidade_item != 0:
                print("Quantidade armazenada com sucesso em sua Lista. \n")
                quantidade_itens.append(quantidade_item)
                break
            else:
                print("Porfavor coloque uma quantidade diferente de 0!")
        except ValueError:
            print("Porfavor, digite um número Inteiro válido!")

# limpa o Terminal

os.system('cls' if os.name == 'nt' else 'clear')

# Imprimindo os dados coletados na Lista

print("-"*80)
print("")
print("Lista de Compras:".center(80))
print("")

for i in range(quantidade):
    print(itens[i], "-", quantidade_itens[i])

print("")
print("-"*80)

        
