import os, time
os.system('cls' if os.name == 'nt' else 'clear')

# Lista das pessoas e idades

pessoas = []
idades = []

# Pedindo as informaçoes necessarias

i = 0

while True:
    print("-" * 80)
    print("")

    # Validação do nome (repete até o nome ser válido)
    while True:
        nome = input(f"Qual é o nome da {i+1}º pessoa a ser cadastrada? ").strip()
        if nome == "":
            print("Campo vazio. Por favor, digite um nome válido!\n")
        else:
            print("Nome cadastrado com sucesso!\n")
            pessoas.append(nome)
            break

    while True:
        try:
            idade = int(input(f"Qual é a idade da {i+1}º pessoa Cadastrada? "))
            if idade <= 0:
                print("Porfavor digite uma idade maior e diferente de zero! \n")
            elif idade > 120: # 120 é a idade da pessoa mais velha do mundo!
                print("Porfavor digite uma idade válida! \n")
            else:
                idades.append(idade)
                print("Salvando informaçoes no banco de dados...")
                time.sleep(3)  
                break
        except ValueError:
            print("Porfavor digite um valor inteiro válido! \n")

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Continuar ou sair

    i += 1 # Adiciona um a mais no final do contador

    print("-"*80)
    print("")
    continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().lower() # Ignora espaços e iguala letras maiusculas e minusculas
    if continuar != 's':
        break

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Exibindo os dados cadastrados

print("")
print("-"*80)
print("")
print("Lista de pessoas cadastradas:".center(80))
print("")

for j in range(len(pessoas)): # Le a quantidade de itnes na lista pessoas!
    print(f"{j+1}. {pessoas[j]} - {idades[j]} anos")

print("")
print("-"*80)

