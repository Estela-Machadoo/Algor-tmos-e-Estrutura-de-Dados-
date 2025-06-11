import os
from Fila import Fila

fila = Fila()

op = -1

while op != 0:
    os.system('cls')
    print("-------------------------")
    print("1 - Adicionar na Fila")
    print("2 - Remover da Fila")
    print("3 - Imprimir Fila")
    print("0 - Sair")
    op = int( input("Digite sua opção: "))
    if op == 1:
        dado = input("Digite o valor que será inserido na Fila: ")
        fila.add( dado )
    elif op == 2:
        fila.remover()
    elif op == 3:
        fila.imprimir()
    elif op != 0:
        print( "Opção Inválida!") 
    input("Enter para continuar...")

# implemente uma fila de carros em um Lava-Jato
# contendo um método para registrar a entrada
# dos carros e uma método para lavar os carros
# O carro deve conter os atributos
# modelo, ano e placa
# desenvolva também um método para imprimir a 
# fila de carros