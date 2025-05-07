from Aluno import Aluno

def main():
    print("=== Cadastro de Aluno ===")
    
    nome = input("Digite seu nome: ")
    cpf = input("Digite o CPF do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")

    aluno = Aluno(nome, cpf, matricula)

    print("\n=== Dados do Aluno ===")
    print("Nome:", aluno.nome)  
    print("CPF:", aluno._cpf)  
    print("Matrícula:", aluno.get_matricula())

    print("\nMarcando presença...")
    aluno.marcarPresenca()

if __name__ == "__main__":
    main()

