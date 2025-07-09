from Torre import Torre
from Apartamento import Apartamento
from Fila_vagas import Fila_vagas

torres = []
apartamentos = []
fila = Fila_vagas()

op = -11

while op != 0:
        print("\n--- MENU CONDOMÍNIO ---")
        print("1 - Cadastrar Torre")
        print("2 - Cadastrar Apartamento")
        print("3 - Adicionar Apto à Fila de Espera")
        print("4 - Remover da Fila")
        print("5 - Imprimir Fila")
        print("0 - Sair")
        op = int( input("Digite sua opção: "))

        if op == 1:
            id = input("ID da Torre: ")
            nome = input("Nome da Torre: ")
            endereco = input("Endereço: ")
            torres.append(Torre(id, nome, endereco))
            print("Torre cadastrada!")

        if op == 2:
            id = input("ID do Apto: ")
            numero = input("Número do Apto: ")
            for i, t in enumerate(Torre):
                print(f"{i}. {t.nome}")
            idx_torre = int(input("Escolha a torre: "))
            apto = Apartamento(id, numero, Torre[idx_torre])
            apartamentos.append(apto)
            print("Apartamento cadastrado!")

        if op == 3:
          dado = input("Digite o valor que será inserido na Fila: ")
          fila.add( dado )
        
        elif op == 4:
          fila.remover()

        elif op == 5:
            fila.imprimir()

        elif op == 0:
            break
        else:
            print("Opção inválida.")
        input("Enter para continuar...")

