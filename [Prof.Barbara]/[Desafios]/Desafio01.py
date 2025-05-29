import os
os.system('cls' if os.name == 'nt' else 'clear')

# Lista de Usuarios, Palestra e Ano de nascimento

usuarios = []
palestras = []
nascimento = []

# Quantidade de usuarios a cadastrar

while True:
    try:
        print("-"*80)
        print("")
        quantidade = int(input("Quantidade de usuarios a cadastrar: "))
        print("")
        print("-"*80, "\n")
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

# Pedindo as informações dos participantes

for i in range(quantidade):
    while True:
        nome = input(f"Digite o nome do {i+1}º participante: ")

        if nome.strip() == "":
            print("Nome inválido. Digite um nome válido.")
        else:
            print("Nome cadastrado com sucesso. \n")
            usuarios.append(nome)
            break

    while True:
        palestra = input(f"Qual é a palestra que o {i+1}º participante participará? ")

        if nome.strip() == "":
            print("Palestra inválida. Porfavor não deixe o campo em branco.")
        else:
            print("Palestra cadastrada com sucesso. \n")
            palestras.append(palestra)
            break

    while True:
        try:
            ano = int(input(f"Qual é o ano de nascimento do {i+1}º participante? "))

            if ano > 1900 and ano < 2025:
                print("Ano de nascimento cadastrado com sucesso. \n")
                nascimento.append(ano)
                break
            else:
                print("Ano de nascimento inválida. Digite um ano entre 1900 e 2025.")
        except ValueError:
                print("Ano de nascimento inválido. Digite um número inteiro.")

# Limpar o terminal para melhor visualização

os.system("cls")

# Imprimindo os dados coletados na Lista

print("-"*80)
print("")
print("Dados coletados:".center(80))
print("")

for i in range(quantidade):
    print(usuarios[i], "-", palestras[i], "-", nascimento[i])

print("")
print("-"*80)