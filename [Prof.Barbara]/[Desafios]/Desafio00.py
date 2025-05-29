import os
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    banco = ""
    nome = ""
    opcao = 0
    while True:
        print("-"*40)
        print("")
        print("Cadastro Bancario".center(40))
        print("")
        print("[1].Cadastrar Instituição Financeira.")
        print("[2].Cadastrar Cliente.")
        print("[3].Ver informaçoes cadastradas.")
        print("[4].Sair do Sistema.")
        print("")
        print("-"*40)


        print("")
        opcao=int(input("Escolha uma opção: "))
        print("")


        if opcao == 1:  
            banco = input("Digite o nome da instituição bancaria: ")
            print("")
            print("Dados cadastrados com sucesso!")
            print("")

        elif opcao == 2:
            nome = input("Digite o nome do Cliente: ")
            print("")
            print("Dados cadastrados com sucesso!")
            print("")

        elif opcao == 3:
            if nome == "" or isinstance(nome, int) or banco == isinstance(banco, int) or banco == "":  #.isistance verifica se o cliente ou o banco é um numero exibindo uma mensagem de erro!
                print("")
                print("Nenhum dado cadastrado!")
                print("")
            else:
                print("-"*40)
                print("")
                print("Dados apurados:")
                print("")
                print(f"Banco: {banco}")
                print(f"Cliente: {nome}")
                print("")

        elif opcao == 4:
            print("-"*40)
            print("")
            print("Encerrando o sistema...")
            print("")
            print('-'*40)
            print("")
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()