import os, time
os.system('cls' if os.name == 'nt' else 'clear')

# Peindo o saldo bancario do usuario

while True:
    try:
        print("-"*80)
        print("")
        saldo = float(input("Qual é o saldo disponivel em sua conta? ").replace(",","."))
        print("")
        print("-"*80)
        break
    except ValueError:
        print("Porfavor digite um valor válido! \n")

# Valor a sacar

while True:
    try:
        valor_sacar = float(input("\nQual é o valor que você deseja sacar? ").replace(",","."))
        if valor_sacar > saldo:
            print("Saldo insuficiente! Insira um valor que não ultrapasse o seu saldo disponível. \n")
        elif valor_sacar < 2:
            print("O Valor mínimo de saque é de R$2,00")
        else:
            break
    except ValueError:
        print("Porfavor digite um valor válido!")

# Saldo Restante

saldo_restante = saldo - valor_sacar

# limpar terminal

os.system('cls' if os.name == 'nt' else 'clear')

# Lista com as cedulas disponiveis

notas = [100, 50, 20, 10, 5, 2]

# Contador de notas com base no sauqe

print("-"*80)
print("")
print("BANCO GUERRA - 24Hrs".center(80))
print(f"Contabilizando as notas para o saque de R${valor_sacar}".center(80))
print("")
print("-"*80)
print("")

time.sleep(3)

for nota in notas:
    quantidade = valor_sacar // nota
    valor_sacar = valor_sacar % nota
    quantidade_int = int(quantidade)
    if quantidade > 0:
        print(f"{quantidade_int} nota(s) de R${nota}".center(80))

saque_restante = valor_sacar
saque_restante = round(saque_restante, 2)

print("")
print("Retire o seu dinheiro. Obrigado pela preferência".center(80))
print(f"Saldo restante não sacado R${saque_restante}".center(80))
print(f"Saldo restante em conta R${saldo_restante}".center(80))
print("")
print("-"*80)
