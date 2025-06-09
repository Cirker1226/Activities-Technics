import os
os.system('cls' if os.name == 'nt' else 'clear')

# Listas funcionais

veiculos = []
tempos = []

# Pedindo informações dos veículos a entrar

i = 0

while True:
    print("-" * 80)
    print("")
    print("LMA Garagem - 24Hrs".center(80))
    print("")
    print("-" * 80)
    print("")

    while True: 
        veiculo = input(f"Qual é o modelo do {i+1}º veículo a entrar? ").strip()    
        if veiculo == "":
            print("Campo Vazio. Por favor digite um modelo de veículo.\n")
        else:
            print("Veículo salvo com sucesso!\n")
            veiculos.append(veiculo)
            break

    while True:
        try:
            tempo = int(input(f"Quantas horas o {i+1}º veículo vai ficar no estacionamento? ").strip())
            if tempo <= 0:
                print("Por favor, digite um valor maior do que 0!\n")
            else:
                print("Tempo salvo com sucesso!\n")
                tempos.append(tempo)
                break
        except ValueError:
            print("Por favor, digite um valor válido!")

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
print("LMA Garagem - 24Hrs".center(80))
print("")
print("-" * 80)
print("")
print("Veículos Cadastrados:".center(80))
print("")

for i in range(len(veiculos)):
    print(f"{i+1}º: {veiculos[i]} - {tempos[i]} horas")

print("")
print("-"*80)

# Número total de veículos cadastrados

total_veiculos = len(veiculos)
print(f"\nTotal de veículos cadastrados: {total_veiculos}")

# Convertendo horas para dias

tempos_em_dias = [t / 24 for t in tempos] # Equação para converter horas para dias
media_dias = sum(tempos_em_dias) / total_veiculos # Dica: SUM - usado para somar tudo da lista

print(f"Média de dias que os veículos permanecerão na garagem: {media_dias:.2f} dias")

# Veículo que ficará mais tempo

maior_tempo = max(tempos) # Dica: Max - retorna o maior valor dentro da lista
indice_mais_tempo = tempos.index(maior_tempo)
veiculo_mais_tempo = veiculos[indice_mais_tempo] # Pega o veiculo com maior Tempo.

print(f"Veículo que ficará mais tempo: {veiculo_mais_tempo} ({maior_tempo} horas = {maior_tempo / 24:.2f} dias.)")

print("")
print("-"*80)
