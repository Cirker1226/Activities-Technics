import os
os.system('cls' if os.name == 'nt' else 'clear')

# Listas

nomes = []
notas = []

# Peindo as informaçoes do Aluno

n = 0

while True:
    print("-" * 80)
    print("")
    print("Instituto Educacional Missão Paz".center(80))
    print("")
    print("-" * 80)
    print("")

    while True: 
        nome = input(f"Qual é o nome do {n+1}º aluno? ").strip()
        if nome == "":
            print("Campo vazio. Por favor, digite um nome válido!\n")
        else:
            print("Nome cadastrado com sucesso!\n")
            nomes.append(nome)
            break
    
    while True:
        try:
            nota = int(input(f"Qual é a nota do {n+1}º aluno? "))
            if nota < 0:
                print("Porfavor digite uma nota válida!\n")
            elif nota == "":
                print("Campo vazio. Por favor, digite uma nota válida!\n")
            else:
                print("Nota cadastrada com sucesso!\n")
                notas.append(nota)
                break
        except ValueError:
            print("Porfavor digite um valor inteiro válido")

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Continuar ou sair

    n = n + 1  # Incrementa o contador de alunos

    print("-"*80)
    print("")

    continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().lower()
    if continuar != 's':
        break

# Limpando terminal

    os.system('cls' if os.name == 'nt' else 'clear')

# Exibindo os dados cadastrados

print("")
print("-"*80)
print("")
print("Alunos e Notas cadastradas:".center(80))
print("")

for j in range(len(nomes)):
    print(f"{j+1}. {nomes[j]} - {notas[j]}")

print("")
print("-"*80)

# Contabilizar número total de alunos

total_alunos = len(nomes)
print(f"\nTotal de alunos cadastrados: {total_alunos}")

# Calcular média das notas

if total_alunos > 0:
    media_notas = sum(notas) / total_alunos
    print(f"Média da turma: {media_notas:.2f}")

# Encontrar aluno com maior nota
    
    maior_nota = max(notas) 
    indice_maior = notas.index(maior_nota)
    aluno_maior_nota = nomes[indice_maior]
    print(f"Aluno com a maior nota: {aluno_maior_nota} ({maior_nota})")
else:
    print("Nenhum aluno cadastrado.")

print("")
print("-"*80)



    