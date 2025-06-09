import os
os.system('cls' if os.name == 'nt' else 'clear')

# Listas

livros = []
anos = []
condiçoes = []

# Pedindo informaçoes dos livros

i = 0

while True:
    print("-"*80)
    print("")
    print("Biblioteca - LMA".center(80))
    print("")
    print("-"*80)
    print("")

    while True:
        titulo = input(f"Qual é o titulo do {i+1}º Livro? ").strip()
        if titulo == "":
            print("Campo vazio. Por favor, digite um livro válido!\n")
        else:
            print("Livro cadastrado com sucesso!\n")
            livros.append(titulo)
            break

    while True:
        try:
            ano = int(input(f"Qual é o ano de lançamento do {i+1}º livro? "))
            if ano == 0 or ano == "":
                print("Porfavor digite um ano válido!\n")
            else:
                print("Ano cadastrado com sucesso!\n")
                anos.append(ano)
                break
        except ValueError:
            print("Porfavor digite um ano válido!\n")
    
    while True:
        condicao = input(f"Qual é o estado do {i+1}º livro(novo/usado)? ").strip().lower()
        if condicao not in ["novo", "usado"]:
            print("Entrada inválida! Por favor, digite apenas 'novo' ou 'usado'.\n")
        else:
            print(f"Estado do livro cadastrado com sucesso!\n")
            condiçoes.append(condicao)
            break

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
print("Biblioteca - LMA".center(80))
print("")
print("-" * 80)
print("")
print("Livros Cadastrados:".center(80))
print("")

for i in range(len(livros)):
    print(f"{i+1}º: {livros[i]} - {anos[i]} - {condiçoes[i]}")

print("")
print("-"*80)

# Número total de livros cadastrados.

total_livros = len(livros)
print(f"\nTotal de veículos cadastrados: {total_livros}")

# Quantidade de livros novos

quantidade_novos = condiçoes.count("novo")
print(f"Quantidade de livros novos: {quantidade_novos}")

# Livro mais antigo

ano_mais_antigo = min(anos)
indice_mais_antigo = anos.index(ano_mais_antigo)
livro_mais_antigo = livros[indice_mais_antigo]

print(f"O livro mais antigo é '{livro_mais_antigo}', lançado em {ano_mais_antigo}.")
print("")
print("-"*80)
            